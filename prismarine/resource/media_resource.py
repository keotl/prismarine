from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET
from jivago.wsgi.request.partial_content_handler import PartialContentHandler
from jivago.wsgi.request.request import Request
from jivago.wsgi.request.response import Response

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.filesystem.media.track_transcoder import TrackTranscoder
from prismarine.media_info.media_library import MediaLibrary


@Resource("/media")
class MediaResource(object):

    @Inject
    def __init__(self, artwork_repository: CoverArtRepository, media_library: MediaLibrary, partial_content_handler: PartialContentHandler,
                 track_transocder: TrackTranscoder):
        self.track_transocder = track_transocder
        self.partial_content_handler = partial_content_handler
        self.media_library = media_library
        self.artwork_repository = artwork_repository

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: str, request: Request) -> Response:
        track = self.media_library.get_track(UUID(track_id))
        transcoded_track_file = self.track_transocder.transcode_track(track)
        return self.partial_content_handler.handle_partial_content_request(request, transcoded_track_file)

    @GET
    @Path("/artwork/{album_id}")
    def get_album_artwork(self, album_id: str) -> Response:
        artwork = self.artwork_repository.get_artwork(UUID(album_id))
        return Response(200, {'Content-Type': artwork.mime_type}, artwork.data)
