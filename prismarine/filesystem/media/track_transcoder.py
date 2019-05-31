import subprocess

from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject

from prismarine.configuration.transcoding_settings import TranscodingSettings


@Component
class TrackTranscoder(object):

    @Inject
    def __init__(self, transcoding_settings: TranscodingSettings):
        self.transcodedFileFolder = transcoding_settings.transcoded_media_folder
        self.streamingBitrate = transcoding_settings.audio_bitrate

    def transcode(self, source_file: str, destination_file: str):
        command = ["ffmpeg", "-i",
                   f"{source_file}",
                   "-vn",
                   "-acodec", "libopus", "-f", "webm",
                   "-b:a", f"{self.streamingBitrate}",
                   f"{destination_file}"]

        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
