import os
import subprocess
from typing import Tuple
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
        track = self.media_library.get_track(UUID(track_id))
        filename = track.filename
        length = track.length


        total_filesize = os.path.getsize(filename)
        start, end = self._parse_range_string(request.headers['HTTP_RANGE'], 200000, total_filesize)
        file, start, end = self._read_transcode(filename, start, end-start)
        return Response(206, {"Content-Type": "application/octet-stream", "Accept-Ranges": "bytes",
                              "Content-Range": f"bytes {start}-{end - 1}/{int(length * 256000)}"}, file)


    @GET
    @Path("/artwork/{album_id}")
    def get_album_artwork(self, album_id: str) -> Response:
        artwork = self.artwork_repository.get_artwork(UUID(album_id))
        return Response(200, {'Content-Type': artwork.mime_type}, artwork.data)

    def _read_transcode(self, file, start, delta) -> Tuple[bytes, int, int]:
        # file = "/home/atreides/Music/Paramore/Paramore/09 Still Into You.m4a"
        # start = 1
        # delta = 30

        command = ["ffmpeg", "-i",
                   f"{file}",
                   "-ss", f"{(start - 1000)/32000}",
                   "-vn",
                   "-flags", "bitexact",
                   "-b:a", "256k",
                   "-acodec", "libopus", "-t", "10", "-f", "webm", "-"]

        pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10 ** 8)
        read_stuff = pipe.stdout.read()

        print(f"read_stuff: {len(read_stuff)}")
        pipe.terminate()
        return read_stuff, start, int(start + len(read_stuff))

    def _parse_range_string(self, range_string: str, default_block_size: int, file_end_offset: int) -> Tuple[int, int]:
        start = int(range_string.split("=")[1].split("-")[0])

        end_string = range_string.split("-")[1]
        end = int(end_string) if end_string != '' else start + default_block_size

        if end > file_end_offset:
            end = file_end_offset

        return start, end
