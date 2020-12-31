# Prismarine Music Player
![logo](./assets/logo.png)

A self-hosted music streaming app.

## Installation
### Linux (Ubuntu, Debian)
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

