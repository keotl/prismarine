from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource
from jivago.wsgi.methods import POST, PUT
from prismarine.services.playback_service import PlaybackService


@Resource("/playback")
class PlaybackResource(object):

    @Inject
    def __init__(self, playback_service: PlaybackService):
        self.playback_service = playback_service

    @POST
    def create_playback(self):

        return self.playback_service.create_playback()

    @PUT
    def modify_playback(self):
        raise NotImplementedError
