from typing import List

from jivago.lang.annotations import Serializable

from prismarine.resource.model.search.artist_result import ArtistResult


@Serializable
class ArtistSearch(object):

    def __init__(self, artists: List[ArtistResult]):
        self.artists = artists
