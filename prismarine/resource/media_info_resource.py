from jivago.lang.annotations import Inject
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.invocation.parameters import PathParam
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.album_mapper import AlbumMapper
from prismarine.resource.mapper.artist_mapper import ArtistMapper
from prismarine.resource.mapper.track_mapper import TrackMapper
from prismarine.resource.model.album_model import AlbumModel
from prismarine.resource.model.artist_model import ArtistModel
from prismarine.resource.model.track_model import TrackModel


@Resource("/info")
class MediaInfoResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, album_mapper: AlbumMapper, track_mapper: TrackMapper, artist_mapper: ArtistMapper):
        self.artist_mapper = artist_mapper
        self.track_mapper = track_mapper
        self.media_library = media_library
        self.album_mapper = album_mapper

    @GET
    @Path("/album/{album_id}")
    def get_album(self, album_id: PathParam[str]) -> AlbumModel:
        album = self.media_library.get_album(str(album_id))
        return self.album_mapper.to_model(album)

    @GET
    @Path("/track/{track_id}")
    def get_track(self, track_id: PathParam[str]) -> TrackModel:
        track = self.media_library.get_track(str(track_id))
        return self.track_mapper.to_model(track)

    @GET
    @Path("/artist/{artist_id}")
    def get_artist(self, artist_id: PathParam[str]) -> ArtistModel:
        artist = self.media_library.get_artist(str(artist_id))
        return self.artist_mapper.to_model(artist)
