from jivago.lang.annotations import Inject
from jivago.lang.registry import Component

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.album_info import AlbumInfo
from prismarine.resource.model.search.album_result import AlbumResult


@Component
class AlbumSearchMapper(object):

    @Inject
    def __init__(self, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository

    def to_model(self, album_info: AlbumInfo) -> AlbumResult:
        return AlbumResult(
            str(album_info.id),
            album_info.name,
            album_info.artist,
            album_info.release_year,
            "/media/artwork/{}".format(album_info.id) if self.artwork_repository.has_artwork_for(
                album_info.id) else ''
        )
