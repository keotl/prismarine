#!/bin/sh
rm -rf build
mkdir build
git clone https://github.com/keotl/prismarine-ui.git build/ui
cd build/ui && npm install && npm run build && cd ../..

mkdir -p build/prismarine/DEBIAN build/prismarine/usr/lib/prismarine-server/static build/prismarine/etc/nginx/sites-available
cp -r build/ui/dist/* build/prismarine/usr/lib/prismarine-server/static
cp -r prismarine build/prismarine/usr/lib/prismarine-server
cp main.py build/prismarine/usr/lib/prismarine-server
cp application.yml build/prismarine/usr/lib/prismarine-server
cp requirements.txt build/prismarine/usr/lib/prismarine-server

cp deploy/debian/control build/prismarine/DEBIAN
cp deploy/debian/postinst build/prismarine/DEBIAN
cp deploy/debian/nginx.conf build/prismarine/etc/nginx/sites-available/prismarine
