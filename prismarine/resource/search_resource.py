import urllib.parse

from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream
from jivago.wsgi.annotations import Resource, Path
from jivago.wsgi.methods import GET

from prismarine.media_info.media_library import MediaLibrary
from prismarine.resource.mapper.track_mapper import TrackMapper
from prismarine.resource.model.track_search import TrackSearch


@Resource("/search")
class SearchResource(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, track_mapper: TrackMapper):
        self.track_mapper = track_mapper
        self.media_library = media_library

    @GET
    @Path("/tracks")
    def search_by_track_title(self, q: str) -> TrackSearch:
        tracks = self.media_library.search_tracks_by_title(q)
        return TrackSearch(Stream(tracks).map(lambda t: self.track_mapper.to_model(t)).toList())
