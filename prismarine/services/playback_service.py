from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject

from prismarine.playback.playback_identifier import PlaybackIdentifier
from prismarine.playback.playback_repository import PlaybackRepository


@Component
class PlaybackService(object):

    @Inject
    def __init__(self, playback_repository: PlaybackRepository):
        self.playback_repository = playback_repository

    def create_playback(self):
        id = PlaybackIdentifier()
        self.playback_repository.save_playback(id, [])
        return id

    def get_playback(self, id: PlaybackIdentifier):
        return self.playback_repository.get_playback(id)

