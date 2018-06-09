from typing import List

from prismarine.media_info.album_info import AlbumInfo
from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.track_info import TrackInfo


class ArtistInfo(MediaInfo):

    def __init__(self, id, name: str, albums: List[AlbumInfo], popular_tracks: List[TrackInfo]):
        self.name = name
        self.popular_tracks = popular_tracks
        self.albums = albums
        super().__init__(id)

    def add_album(self, album: AlbumInfo):
        self.albums.append(album)
