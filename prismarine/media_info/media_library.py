from typing import List
from uuid import UUID

from prismarine.media_info.album_info import AlbumInfo
from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.track_info import TrackInfo


class MediaLibrary(object):

    def save_track(self, media: MediaInfo):
        raise NotImplementedError

    def search_tracks_by_title(self, query: str) -> List[TrackInfo]:
        raise NotImplementedError

    def search_albums(self, query: str) -> List[AlbumInfo]:
        raise NotImplementedError

    def get_album(self, id: UUID) -> AlbumInfo:
        raise NotImplementedError

    def get_track(self, id: UUID) -> TrackInfo:
        raise NotImplementedError

    def get_album_for_track(self, track_id: UUID) -> AlbumInfo:
        raise NotImplementedError
