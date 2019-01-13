from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.media_info.track_info import TrackInfo
from prismarine.resource.model.track_model import TrackModel


@Component
class TrackMapper(object):

    @Inject
    def __init__(self, artwork_repository: CoverArtRepository):
        self.artwork_repository = artwork_repository

    def to_model(self, track_info: TrackInfo) -> TrackModel:
        return TrackModel(str(track_info.id),
                          track_info.title,
                          str(track_info.album_id),
                          track_info.genre,
                          track_info.artist,
                          track_info.length,
                          track_info.track_number,
                          track_info.disc_number,
                          '/media/artwork/{}'.format(track_info.album_id) if self.artwork_repository.has_artwork_for(
                              track_info.album_id) else '',
                          track_info.album)
