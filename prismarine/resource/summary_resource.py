from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.album_search_mapper import AlbumSearchMapper
from prismarine.resource.mapper.artist_search_mapper import ArtistSearchMapper
from prismarine.resource.model.search.album_search import AlbumSearch
from prismarine.resource.model.search.artist_search import ArtistSearch


@Resource("/summary")
class SummaryResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, album_mapper: AlbumSearchMapper, artist_mapper: ArtistSearchMapper):
        self.artist_mapper = artist_mapper
        self.album_mapper = album_mapper
        self.media_library = media_library

    @GET
    @Path("/albums")
    def get_albums(self) -> AlbumSearch:
        albums = Stream(self.media_library.get_all_albums()).map(lambda album: self.album_mapper.to_model(album)).toList()

        return AlbumSearch(albums)

    @GET
    @Path("/artists")
    def get_artists(self) -> ArtistSearch:
        artists = Stream(self.media_library.get_all_artists()).map(lambda artist: self.artist_mapper.to_model(artist)).toList()

        return ArtistSearch(artists)
