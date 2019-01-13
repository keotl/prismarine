import glob
import os

from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.filesystem.media.last_fm_image_provider import LastFmImageProvider
from prismarine.filesystem.media.local_folder_artwork_reader import LocalFolderArtworkReader
from prismarine.filesystem.tags.artwork_reader import ArtworkReader
from prismarine.filesystem.tags.metadata_reader import MetadataReader
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.album_info import AlbumInfo
from prismarine.media_info.artist_info import ArtistInfo
from prismarine.media_info.media_library import MediaLibrary


@Component
class MediaIndexer(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, metadata_reader: MetadataReader,
                 artwork_repository: CoverArtRepository, artwork_reader: ArtworkReader,
                 local_folder_artwork_reader: LocalFolderArtworkReader, last_fm_image_provider: LastFmImageProvider):
        self.last_fm_image_provider = last_fm_image_provider
        self.local_folder_artwork_reader = local_folder_artwork_reader
        self.artwork_reader = artwork_reader
        self.artwork_repository = artwork_repository
        self.metadata_reader = metadata_reader
        self.media_library = media_library

    def index_tracks(self, folder_path: str):
        files = Stream(glob.glob(os.path.join(folder_path, '**/*'), recursive=True)).filter(
            lambda path: os.path.isfile(path)).toList()

        for file in files:
            if self.media_library.contains_file(file):
                continue
            try:
                track_info = self.metadata_reader.read_metadata(file)
                self.media_library.save_track(track_info)
                album = self.media_library.get_album_for_track(track_info.id)

                if not self.artwork_repository.has_artwork_for(album.id):
                    self.fetch_and_save_album_artwork(album, file)
                if not self.artwork_repository.has_artwork_for(album.artist_id):
                    self.fetch_and_save_artist_artwork(self.media_library.get_artist(album.artist_id))

            except UnknownAudioFileFormatException:
                continue

    def fetch_and_save_album_artwork(self, album: AlbumInfo, track_file: str):
        artwork = self.artwork_reader.get_artwork(track_file)
        if artwork is None:
            artwork = self.local_folder_artwork_reader.get_artwork(album)
        if artwork is not None:
            self.artwork_repository.save(album.id, artwork)

    def fetch_and_save_artist_artwork(self, artist: ArtistInfo):
        artist_artwork = self.last_fm_image_provider.get_artist_image(artist.name)

        if artist_artwork is not None:
            self.artwork_repository.save(artist.id, artist_artwork)
