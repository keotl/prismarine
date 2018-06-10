from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.artist_info import ArtistInfo
from prismarine.resource.mapper.album_search_mapper import AlbumSearchMapper
from prismarine.resource.model.artist_model import ArtistModel


@Component
class ArtistMapper(object):

    @Inject
    def __init__(self, album_search_mapper: AlbumSearchMapper, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository
        self.album_search_mapper = album_search_mapper

    def to_model(self, artist: ArtistInfo) -> ArtistModel:
        return ArtistModel(
            str(artist.id),
            artist.name,
            Stream(artist.albums).map(lambda album: self.album_search_mapper.to_model(album)).toList(),
            '/media/artwork/{}'.format(artist.id) if self.artwork_repository.has_artwork_for(artist.id) else '',
        )
