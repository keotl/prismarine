import os
import uuid
from typing import List

from jivago.inject.registry import Singleton
from jivago.lang.annotations import Override, Inject
from jivago.lang.stream import Stream

from prismarine.media_info.album_info import AlbumInfo
from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.media_library import MediaLibrary
from prismarine.media_info.no_such_album_exception import NoSuchAlbumException
from prismarine.media_info.no_such_track_exception import NoSuchTrackException
from prismarine.media_info.track_info import TrackInfo


@Singleton
class InMemoryMediaLibrary(MediaLibrary):

    @Inject
    def __init__(self):
        self.content = {'tracks': {}, 'albums': {}}

    @Override
    def save_track(self, media: MediaInfo):
        if media.id is None:
            media.id = uuid.uuid4()
        if isinstance(media, TrackInfo):
            self.content['tracks'][media.id] = media
            self.link_album(media)

    def link_album(self, track: TrackInfo):
        for album in self.content['albums'].values():
            if album.should_contain(track):
                album.add_track(track)
                return
        new_album = AlbumInfo(uuid.uuid4(), track.album, track.artist, os.path.dirname(track.filename),
                              track.total_tracks)
        new_album.add_track(track)
        self.content['albums'][new_album.id] = new_album

    @Override
    def search_tracks_by_title(self, query: str) -> List[TrackInfo]:
        return Stream(self.content['tracks'].values()).filter(
            lambda track: query.lower() in track.title.lower()).toList()

    @Override
    def search_albums(self, query: str) -> List[AlbumInfo]:
        return Stream(self.content['albums'].values()).filter(lambda a: query.lower() in a.name.lower()).toList()

    @Override
    def get_album(self, id) -> AlbumInfo:
        if id in self.content['albums']:
            return self.content['albums'][id]
        else:
            raise NoSuchAlbumException(id)

    @Override
    def get_track(self, id) -> TrackInfo:
        if id in self.content['tracks']:
            return self.content['tracks'][id]
        else:
            raise NoSuchTrackException(id)
