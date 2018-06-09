from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.album_search_mapper import AlbumSearchMapper
from prismarine.resource.mapper.artist_search_mapper import ArtistSearchMapper
from prismarine.resource.mapper.track_search_mapper import TrackMapper
from prismarine.resource.model.search.album_search import AlbumSearch
from prismarine.resource.model.search.artist_search import ArtistSearch
from prismarine.resource.model.search.track_search import TrackSearch

MAX_RESULTS = 4


@Resource("/search")
class SearchResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, track_mapper: TrackMapper, album_mapper: AlbumSearchMapper, artist_mapper: ArtistSearchMapper):
        self.artist_mapper = artist_mapper
        self.album_mapper = album_mapper
        self.track_mapper = track_mapper
        self.media_library = media_library

    @GET
    @Path("/tracks")
    def search_by_track_title(self, q: str) -> TrackSearch:
        tracks = self.media_library.search_tracks_by_title(q)
        if len(tracks) > MAX_RESULTS:
            tracks = tracks[:MAX_RESULTS]
        return TrackSearch(Stream(tracks).map(lambda t: self.track_mapper.to_model(t)).toList())

    @GET
    @Path("/albums")
    def search_by_album(self, q: str) -> AlbumSearch:
        albums = self.media_library.search_albums(q)
        if len(albums) > MAX_RESULTS:
            albums = albums[:MAX_RESULTS]

        return AlbumSearch(Stream(albums).map(lambda a: self.album_mapper.to_model(a)).toList())

    @GET
    @Path("/artists")
    def search_by_artist(self, q: str) -> ArtistSearch:
        artists = self.media_library.search_artists(q)
        if len(artists) > MAX_RESULTS:
            artists = artists[:MAX_RESULTS]

        return ArtistSearch(Stream(artists).map(lambda a: self.artist_mapper.to_model(a)).toList())
