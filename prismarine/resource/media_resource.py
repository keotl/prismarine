from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET
from jivago.wsgi.request.request import Request
from jivago.wsgi.request.response import Response

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.filesystem.media.media_file_retriever import MediaFileRetriever


@Resource("/media")
class MediaResource(object):

    @Inject
    def __init__(self, media_file_retriever: MediaFileRetriever, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository
        self.media_file_retriever = media_file_retriever

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: str, request: Request) -> Response:
        if request.headers['HTTP_RANGE']:
            total_size = self.media_file_retriever.get_track_file_size(UUID(track_id))
            http_range = request.headers['HTTP_RANGE']
            start = int(http_range.split("=")[1].split("-")[0])
            end = start + 2000000 if http_range.split("-")[1] == '' else int(http_range.split("-")[1])
            body = self.media_file_retriever.get_partial_track(UUID(track_id), start, end)
            if end > total_size:
                end = total_size - 1
            return Response(206, {"Content-Type": "application/octet-stream", "Accept-Ranges": "bytes",
                                  "Content-Range": "bytes {}-{}/{}".format(start, end, total_size)},
                            body)
        body = self.media_file_retriever.get_track(UUID(track_id))
        return Response(200, {"Content-Type": "application/octet-stream"}, body)

    @GET
    @Path("/artwork/{album_id}")
    def get_album_artwork(self, album_id: str) -> Response:
        artwork = self.artwork_repository.get_artwork(UUID(album_id))
        return Response(200, {'Content-Type': artwork.mime_type}, artwork.data)
