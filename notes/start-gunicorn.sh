/usr/lib/prismarine-server/venv/bin/gunicorn prismarine.wsgi:app

cd /usr/lib/prismarine-server
/usr/lib/prismarine-server/venv/bin/gunicorn --bind unix:/tmp/gunicorn.sock prismarine.wsgi:app
