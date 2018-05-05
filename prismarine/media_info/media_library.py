import uuid
from typing import List

from jivago.inject.registry import Singleton, Component
from jivago.lang.stream import Stream

from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.track_info import TrackInfo


@Singleton
@Component
class MediaLibrary(object):
    def __init__(self):
        self.content = {'tracks': {}}

    def save(self, media: MediaInfo):
        if isinstance(media, TrackInfo):
            if media.id is None:
                media.id = uuid.uuid4()
            self.content['tracks'][media.id] = media

    def search_tracks_by_title(self, query: str) -> List[TrackInfo]:
        return Stream(self.content['tracks'].values()).filter(
            lambda track: query.lower() in track.title.lower()).toList()
