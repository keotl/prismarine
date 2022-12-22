import os
import subprocess
import threading
from typing import Dict
import logging
from datetime import datetime, timedelta

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.inject.annotation import Component, Singleton
from jivago.lang.annotations import Inject

from prismarine.media_info.track_info import TrackInfo


@Component
@Singleton
class TrackTranscoder(object):

    @Inject
    def __init__(self, application_properties: ApplicationProperties):
        self.transcodedFileFolder = application_properties["transcoded_media_folder"]
        self.streamingBitrate = application_properties["audio_bitrate"]
        self._cache: Dict[str, dict] = {}
        self._lock = threading.Lock()
        self._logger = logging.getLogger(self.__class__.__name__)

    def transcode_track(self, track_info: TrackInfo) -> str:
        """:returns transcoded file path"""
        transcoded_file_path = self.__path(track_info.id)

        with self._lock:
            if not track_info.id in self._cache:
                self._cache[track_info.id] = {"lock": threading.Lock(), "ttl": datetime.min}

            cache_entry = self._cache[track_info.id]

        with cache_entry["lock"]:
            cache_entry["ttl"] = datetime.utcnow() + DEFAULT_TTL
            if not os.path.exists(transcoded_file_path):
                self.__ffmpeg_convert(track_info.filename, transcoded_file_path)

        return transcoded_file_path

    def cleanup(self):
        with self._lock:
            stale = []
            for k, v in self._cache.items():
                if datetime.utcnow() > v["ttl"]:
                    stale.append(k)

            for track in stale:
                os.remove(self.__path(track))
                del self._cache[track]

        self._logger.info(f"Removed {len(stale)} items from the transcoded media cache.")

    def __path(self, track_id: str):
        return os.path.join(self.transcodedFileFolder, str(track_id))

    def __ffmpeg_convert(self, source_file: str, destination_file: str):
        command = ["ffmpeg", "-i",
                   f"{source_file}",
                   "-vn",
                   "-acodec", "aac", "-f", "mp4",
                   "-b:a", f"{self.streamingBitrate}",
                   f"{destination_file}"]

        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

DEFAULT_TTL = timedelta(hours=1)
