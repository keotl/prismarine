import os
from typing import List

from jivago.inject.annotation import Singleton
from jivago.lang.annotations import Override, Inject
from jivago.lang.stream import Stream
from prismarine.infrastructure.persistence.id_factory import IdFactory

from prismarine.media_info.album_info import AlbumInfo
from prismarine.media_info.artist_info import ArtistInfo
from prismarine.media_info.media_info import MediaInfo
from prismarine.media_info.media_library import MediaLibrary
from prismarine.media_info.no_such_album_exception import NoSuchAlbumException
from prismarine.media_info.no_such_artist_exception import NoSuchArtistException
from prismarine.media_info.no_such_track_exception import NoSuchTrackException
from prismarine.media_info.track_info import TrackInfo


@Singleton
class InMemoryMediaLibrary(MediaLibrary):

    @Inject
    def __init__(self, id_factory: IdFactory):
        self.content = {'tracks': {}, 'albums': {}, 'artists': {}}
        self._id_factory = id_factory

    @Override
    def save_track(self, media: TrackInfo):
        if media.id is None:
            media.id = self._id_factory.create_track_id(media.artist, media.album, media.title)

        self.content['tracks'][media.id] = media
        self.link_album(media)

    def link_album(self, track: TrackInfo):
        for album in self.content['albums'].values():
            if album.should_contain(track):
                album.add_track(track)
                track.set_album_id(album.id)
                self.link_artist(album)
                return
        new_album = AlbumInfo(self._id_factory.create_album_id(track.artist, track.album), track.album, track.artist, os.path.dirname(track.filename),
                              track.total_tracks, track.release_year, track.genre)
        new_album.add_track(track)
        track.set_album_id(new_album.id)
        self.content['albums'][new_album.id] = new_album
        self.link_artist(new_album)

    def link_artist(self, album: AlbumInfo):
        for artist in self.content['artists'].values():
            if artist.name == album.artist:
                if album not in artist.albums:
                    artist.add_album(album)
                    album.set_artist_id(artist.id)
                Stream(album.tracks).forEach(lambda track: track.set_artist_id(artist.id))
                return
        new_artist = ArtistInfo(self._id_factory.create_artist_id(album.artist), album.artist, [album], [])
        album.set_artist_id(new_artist.id)
        self.content['artists'][new_artist.id] = new_artist

    @Override
    def search_tracks_by_title(self, query: str) -> List[TrackInfo]:
        return Stream(self.content['tracks'].values()).filter(
            lambda track: query.lower() in track.title.lower()).toList()

    @Override
    def search_albums(self, query: str) -> List[AlbumInfo]:
        return Stream(self.content['albums'].values()).filter(lambda a: query.lower() in a.name.lower()).toList()

    @Override
    def get_album(self, id: str) -> AlbumInfo:
        if id in self.content['albums']:
            return self.content['albums'][id]
        raise NoSuchAlbumException(id)

    @Override
    def get_track(self, id: str) -> TrackInfo:
        if id in self.content['tracks']:
            return self.content['tracks'][id]
        raise NoSuchTrackException(id)

    @Override
    def get_album_for_track(self, track_id: str) -> AlbumInfo:
        track = self.get_track(track_id)
        album = Stream(self.content['albums'].values()).firstMatch(lambda album: album.should_contain(track))
        return album.orElseThrow(NoSuchAlbumException())

    @Override
    def get_artist(self, id: str) -> ArtistInfo:
        if id in self.content['artists']:
            return self.content['artists'][id]
        raise NoSuchArtistException()

    @Override
    def search_artists(self, query: str) -> List[ArtistInfo]:
        return Stream(self.content['artists'].values()).filter(lambda a: query.lower() in a.name.lower()).toList()

    @Override
    def contains_file(self, filename: str) -> bool:
        return Stream(self.content['tracks'].values()).anyMatch(lambda track: track.filename == filename)

    @Override
    def get_all_albums(self) -> List[AlbumInfo]:
        return self.content['albums'].values()

    @Override
    def get_all_artists(self) -> List[ArtistInfo]:
        return self.content['artists'].values()
