from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET
from jivago.wsgi.request.request import Request
from jivago.wsgi.request.response import Response

from prismarine.filesystem.media.media_file_retriever import MediaFileRetriever


@Resource("/media")
class MediaResource(object):

    @Inject
    def __init__(self, media_file_retriever: MediaFileRetriever):
        self.media_file_retriever = media_file_retriever

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: str, request: Request) -> Response:
        body = self.media_file_retriever.get_track(UUID(track_id))
        if request.headers['HTTP_RANGE']:
            http_range = request.headers['HTTP_RANGE']

            start = int(http_range.split("=")[1].split("-")[0])
            end = start + 2000000 if http_range.split("-")[1] == '' else int(http_range.split("-")[1])
            if end > len(body):
                end = len(body) - 1
            return Response(206, {"Content-Type": "application/octet-stream", "Accept-Ranges": "bytes",
                                  "Content-Range": "bytes {}-{}/{}".format(start, end, len(body)),
                                  "Content-Length": end - start + 1},
                            body[start:end + 1])
        return Response(200, {"Content-Type": "application/octet-stream"}, body)
