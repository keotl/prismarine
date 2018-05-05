from jivago.inject.registry import Component

from prismarine.media_info.track_info import TrackInfo
from prismarine.resource.model.track_result import TrackResult


@Component
class TrackMapper(object):

    def to_model(self, track_info: TrackInfo) -> TrackResult:
        return TrackResult(str(track_info.id),
                           track_info.title,
                           track_info.album,
                           track_info.genre,
                           track_info.artist,
                           track_info.length)
