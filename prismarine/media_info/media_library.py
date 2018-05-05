from typing import List

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
