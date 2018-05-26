from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.lang.registry import Component

from prismarine.media_info.media_library import MediaLibrary


@Component
class MediaFileRetriever(object):

    @Inject
    def __init__(self, media_library: MediaLibrary):
        self.media_library = media_library

    def get_track(self, track_id: UUID):
        filename = self.media_library.get_track(track_id).filename
        with open(filename, 'rb') as f:
            return f.read()
