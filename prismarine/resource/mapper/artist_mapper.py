from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.media_info.artist_info import ArtistInfo
from prismarine.resource.mapper.album_search_mapper import AlbumSearchMapper
from prismarine.resource.model.artist_model import ArtistModel


@Component
class ArtistMapper(object):

    @Inject
    def __init__(self, album_search_mapper: AlbumSearchMapper):
        self.album_search_mapper = album_search_mapper

    def to_model(self, artist: ArtistInfo) -> ArtistModel:
        return ArtistModel(
            str(artist.id),
            artist.name,
            Stream(artist.albums).map(lambda album: self.album_search_mapper.to_model(album)).toList()
        )
