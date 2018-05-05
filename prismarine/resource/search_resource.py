from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.album_search_mapper import AlbumSearchMapper
from prismarine.resource.mapper.track_search_mapper import TrackMapper
from prismarine.resource.model.search.album_search import AlbumSearch
from prismarine.resource.model.search.track_search import TrackSearch


@Resource("/search")
class SearchResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, track_mapper: TrackMapper, album_mapper: AlbumSearchMapper):
        self.album_mapper = album_mapper
        self.track_mapper = track_mapper
        self.media_library = media_library

    @GET
    @Path("/tracks")
    def search_by_track_title(self, q: str) -> TrackSearch:
        tracks = self.media_library.search_tracks_by_title(q)
        return TrackSearch(Stream(tracks).map(lambda t: self.track_mapper.to_model(t)).toList())

    @GET
    @Path("/albums")
    def search_by_album(self, q: str) -> AlbumSearch:
        albums = self.media_library.search_albums(q)
        return AlbumSearch(Stream(albums).map(lambda a: self.album_mapper.to_model(a)).toList())
