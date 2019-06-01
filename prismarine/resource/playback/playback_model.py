from typing import List

from jivago.lang.annotations import Serializable


@Serializable
class PlaybackModel(object):

    def __init__(self, id: str, playback: List[str]):
        self.id = id
        self.playback = playback
