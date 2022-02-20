# Prismarine Music Player
![logo](./assets/logo.png)

A self-hosted music streaming app.

# Installation
## Run with docker (Recommended)
```bash
docker run -it -p 5000:5000 \
  --env media_library=/music \
  --mount type=bind,source=/home/user/Music,target=/music,readonly \
  keotl/prismarine:latest
```
Open http://localhost:5000 in your browser.

## Docker compose
```yaml
version: '3'
volumes:
  /home/user/Music: null
services:
  prismarine:
    container_name: prismarine
    deploy:
      replicas: 1
      restart_policy:
        condition: always
    environment:
      media_library: /music
    expose:
    - 5000
    image: keotl/prismarine:1.0.3
    ports:
    - '5000'
    volumes:
    - /home/user/Music:/music:ro
```
## Linux (Ubuntu, Debian)
1. Download the latest stable .deb package from the [releases page](https://github.com/keotl/prismarine/releases).
2. Install the required dependencies.
```bash
sudo apt install ffmpeg nginx python3-pip
```
3. Install the deb package.
```bash
sudo dpkg -i prismarine.deb
```
4. Edit the configuration file to point the server to your media library.
```
sudo nano /usr/lib/prismarine-server/application.yml
```
Modify the `media_library` folder to your liking.

5. Enable/start Prismarine using systemd.
```bash
sudo systemctl enable prismarine
sudo systemctl start prismarine
```
6. Open Prismarine in your browser. The server listens on all interfaces on port 80 by default.

