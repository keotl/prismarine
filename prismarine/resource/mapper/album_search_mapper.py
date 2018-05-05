from jivago.inject.registry import Component

from prismarine.media_info.album_info import AlbumInfo
from prismarine.resource.model.search.album_result import AlbumResult


@Component
class AlbumSearchMapper(object):

    def to_model(self, album_info: AlbumInfo) -> AlbumResult:
        return AlbumResult(
            str(album_info.id),
            album_info.name,
            album_info.artist
        )
