from typing import List

from jivago.lang.annotations import Serializable

from prismarine.resource.model.track_result import TrackModel


@Serializable
class AlbumModel(object):

    def __init__(self, id: str, name: str, artist: str, tracks: List[TrackModel]):
        self.id = id
        self.name = name
        self.artist = artist
        self.tracks = tracks
