from jivago.lang.annotations import Inject
from jivago.lang.registry import Component

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.artist_info import ArtistInfo
from prismarine.resource.model.search.artist_result import ArtistResult


@Component
class ArtistSearchMapper(object):

    @Inject
    def __init__(self, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository

    def to_model(self, artist: ArtistInfo) -> ArtistResult:
        return ArtistResult(
            str(artist.id),
            artist.name,
            '/media/artwork/{}'.format(artist.id) if self.artwork_repository.has_artwork_for(artist.id) else '',
        )
