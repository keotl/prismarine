from typing import List

from jivago.lang.annotations import Serializable

from prismarine.resource.model.album_result import AlbumResult


@Serializable
class AlbumSearch(object):
    
    def __init__(self, albums: List[AlbumResult]):
        self.albums = albums
