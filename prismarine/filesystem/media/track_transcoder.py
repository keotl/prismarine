import os
import subprocess

from jivago.config.properties.application_properties import ApplicationProperties
from jivago.lang.annotations import Inject
from jivago.lang.registry import Component

from prismarine.media_info.track_info import TrackInfo


@Component
class TrackTranscoder(object):

    @Inject
    def __init__(self, application_properties: ApplicationProperties):
        self.transcodedFileFolder = application_properties["transcoded_media_folder"]
        self.streamingBitrate = application_properties["audio_bitrate"]

    def transcode_track(self, track_info: TrackInfo) -> str:
        """:returns transcoded file path"""
        transcoded_file_path = os.path.join(self.transcodedFileFolder, str(track_info.id))
        if not os.path.exists(transcoded_file_path):
            self.__ffmpeg_convert(track_info.filename, transcoded_file_path)
        return transcoded_file_path

    def __ffmpeg_convert(self, source_file: str, destination_file: str):
        command = ["ffmpeg", "-i",
                   f"{source_file}",
                   "-vn",
                   "-acodec", "libopus", "-f", "webm",
                   "-b:a", f"{self.streamingBitrate}",
                   f"{destination_file}"]

        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
