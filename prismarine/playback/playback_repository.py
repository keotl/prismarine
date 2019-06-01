from typing import List
from uuid import UUID

from jivago.inject.annotation import Singleton


@Singleton
class PlaybackRepository(object):

    def get_playback(self, id: UUID):
        raise NotImplementedError

    def save_playback(self, id: UUID, playback: List[UUID]):
        raise NotImplementedError
