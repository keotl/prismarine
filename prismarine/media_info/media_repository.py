from jivago.inject.registry import Singleton, Component

from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.track_info import TrackInfo


@Singleton
@Component
class MediaRepository(object):
    def __init__(self):
        self.content = {'tracks': {}}

    def save(self, media: MediaInfo):
        if isinstance(media, TrackInfo):
            self.content['tracks'][media.id] = media
