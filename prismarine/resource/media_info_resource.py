from uuid import UUID

from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.album_mapper import AlbumMapper
from prismarine.resource.mapper.track_search_mapper import TrackMapper
from prismarine.resource.model.album_model import AlbumModel
from prismarine.resource.model.track_result import TrackModel


@Resource("/info")
class MediaInfoResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, album_mapper: AlbumMapper, track_mapper: TrackMapper):
        self.track_mapper = track_mapper
        self.media_library = media_library
        self.album_mapper = album_mapper

    @GET
    @Path("/album/{album_id}")
    def get_album(self, album_id: str) -> AlbumModel:
        album = self.media_library.get_album(UUID(album_id))
        return self.album_mapper.to_model(album)

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: str) -> TrackModel:
        track = self.media_library.get_track(UUID(track_id))
        return self.track_mapper.to_model(track)

