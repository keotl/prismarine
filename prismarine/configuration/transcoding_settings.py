from jivago.config.properties.application_properties import ApplicationProperties
from jivago.inject.annotation import Provider, Singleton
from multiprocessing import cpu_count


class TranscodingSettings(object):
    transcoded_media_folder: str
    audio_bitrate: str
    transcoding_executors: int


@Provider
@Singleton
def create_transcoding_settings(properties: ApplicationProperties) -> TranscodingSettings:
    settings = TranscodingSettings()
    settings.transcoded_media_folder = properties['transcoded_media_folder']
    settings.audio_bitrate = properties["audio_bitrate"]
    settings.transcoding_executors = cpu_count() if "transcoding_executors" not in properties \
        else int(properties["transcoding_executors"])

    return settings
