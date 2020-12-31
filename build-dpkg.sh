#!/bin/sh
rm -rf build
mkdir build
cd webui && npm install && npm run build && cd ..

mkdir -p build/prismarine/debian build/prismarine/usr/lib/prismarine-server/static build/prismarine/etc/nginx/sites-available build/prismarine/etc/systemd/system
cp -r webui/dist/* build/prismarine/usr/lib/prismarine-server/static
cp -r prismarine build/prismarine/usr/lib/prismarine-server
cp main.py build/prismarine/usr/lib/prismarine-server
cp application.yml build/prismarine/usr/lib/prismarine-server
cp requirements.txt build/prismarine/usr/lib/prismarine-server

cp -r deploy/debian build/prismarine

cp deploy/config/nginx.conf build/prismarine/etc/nginx/sites-available/prismarine
cp deploy/config/prismarine.service build/prismarine/etc/systemd/system/

#TODO remove, directory structure should be created correctly from the start
mv build/prismarine/debian build/prismarine/DEBIAN
sed -i "s/@@VERSION@@/$(git describe --tags)/g" build/prismarine/DEBIAN/control
dpkg-deb --build build/prismarine
