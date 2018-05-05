from typing import List

from jivago.lang.annotations import Serializable

from prismarine.resource.model.track_result import TrackResult


@Serializable
class TrackSearch(object):
    
    def __init__(self, tracks: List[TrackResult]):
        self.tracks = tracks
