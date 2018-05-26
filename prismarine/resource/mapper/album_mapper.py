from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.media_info.album_info import AlbumInfo
from prismarine.resource.mapper.track_search_mapper import TrackMapper
from prismarine.resource.model.album_model import AlbumModel


@Component
class AlbumMapper(object):

    @Inject
    def __init__(self, track_mapper: TrackMapper):
        self.track_mapper = track_mapper

    def to_model(self, album: AlbumInfo) -> AlbumModel:
        tracks = Stream(album.tracks).map(lambda t: self.track_mapper.to_model(t)).toList()
        return AlbumModel(
            str(album.id),
            album.name,
            album.artist,
            tracks
        )
