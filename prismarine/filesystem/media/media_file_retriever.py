import os
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

    def get_partial_track(self, track_id: UUID, start_offset: int, end_offset: int) -> bytes:
        filename = self.media_library.get_track(track_id).filename
        with open(filename, 'rb') as f:
            f.seek(start_offset)
            return f.read(end_offset - start_offset)

    def get_track_file_size(self, track_id: UUID) -> int:
        filename = self.media_library.get_track(track_id).filename
        return os.path.getsize(filename)
