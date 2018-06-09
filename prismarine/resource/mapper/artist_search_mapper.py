from jivago.lang.registry import Component

from prismarine.media_info.artist_info import ArtistInfo
from prismarine.resource.model.search.artist_result import ArtistResult


@Component
class ArtistSearchMapper(object):

    def to_model(self, artist: ArtistInfo) -> ArtistResult:
        return ArtistResult(
            str(artist.id),
            artist.name
        )
