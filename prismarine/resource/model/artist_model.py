from typing import List

from jivago.lang.annotations import Serializable

from prismarine.resource.model.search.album_result import AlbumResult


@Serializable
class ArtistModel(object):

    def __init__(self, id: str, name: str, albums: List[AlbumResult], image_url: str):
        self.image_url = image_url
        self.id = id
        self.name = name
        self.albums = albums
