from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.album_info import AlbumInfo
from prismarine.resource.mapper.track_search_mapper import TrackMapper
from prismarine.resource.model.album_model import AlbumModel


@Component
class AlbumMapper(object):

    @Inject
    def __init__(self, track_mapper: TrackMapper, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository
        self.track_mapper = track_mapper

    def to_model(self, album: AlbumInfo) -> AlbumModel:
        tracks = Stream(album.tracks).map(lambda t: self.track_mapper.to_model(t)).toList()
        tracks.sort(key=lambda t: (t.disc_number, t.track_number))
        return AlbumModel(
            str(album.id),
            album.name,
            album.artist,
            album.release_year,
            tracks,
            "/media/artwork/{}".format(album.id) if self.artwork_repository.has_artwork_for(album.id) else '')
