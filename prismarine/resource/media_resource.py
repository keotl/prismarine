from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET
from jivago.wsgi.partial_content_handler import PartialContentHandler
from jivago.wsgi.request.request import Request
from jivago.wsgi.request.response import Response

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.media_library import MediaLibrary


@Resource("/media")
class MediaResource(object):

    @Inject
    def __init__(self, artwork_repository: CoverArtRepository, media_library: MediaLibrary, partial_content_handler: PartialContentHandler):
        self.partial_content_handler = partial_content_handler
        self.media_library = media_library
        self.artwork_repository = artwork_repository

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: str, request: Request) -> Response:
        filename = self.media_library.get_track(UUID(track_id)).filename
        return self.partial_content_handler.handle_partial_content_request(request, filename)

    @GET
    @Path("/artwork/{album_id}")
    def get_album_artwork(self, album_id: str) -> Response:
        artwork = self.artwork_repository.get_artwork(UUID(album_id))
        return Response(200, {'Content-Type': artwork.mime_type}, artwork.data)
