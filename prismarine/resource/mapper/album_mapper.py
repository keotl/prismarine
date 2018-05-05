from jivago.inject.registry import Component

from prismarine.media_info.album_info import AlbumInfo
from prismarine.resource.model.album_result import AlbumResult


@Component
class AlbumMapper(object):

    def to_model(self, album_info: AlbumInfo) -> AlbumResult:
        return AlbumResult(
            str(album_info.id),
            album_info.name,
            album_info.artist
        )
