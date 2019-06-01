from typing import List
from uuid import UUID

from prismarine.playback.playback_repository import PlaybackRepository


class InMemoryPlaybackRepository(PlaybackRepository):
    def save_playback(self, id: UUID, playback: List[UUID]):
        pass

    def get_playback(self, id: UUID):
        pass
