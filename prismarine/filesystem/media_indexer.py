import glob
import os

from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.filesystem.media.cover_art_repository import CoverArtRepository
from prismarine.filesystem.media.local_folder_artwork_reader import LocalFolderArtworkReader
from prismarine.filesystem.tags.artwork_reader import ArtworkReader
from prismarine.filesystem.tags.metadata_reader import MetadataReader
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.media_library import MediaLibrary


@Component
class MediaIndexer(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, metadata_reader: MetadataReader,
                 artwork_repository: CoverArtRepository, artwork_reader: ArtworkReader,
                 local_folder_artwork_reader: LocalFolderArtworkReader):
        self.local_folder_artwork_reader = local_folder_artwork_reader
        self.artwork_reader = artwork_reader
        self.artwork_repository = artwork_repository
        self.metadata_reader = metadata_reader
        self.media_library = media_library

    def index_tracks(self, folder_path: str):
        files = Stream(glob.glob(os.path.join(folder_path, '**/*'), recursive=True)).filter(
            lambda path: os.path.isfile(path)).toList()

        for file in files:
            try:
                track_info = self.metadata_reader.read_metadata(file)
                self.media_library.save_track(track_info)
                album = self.media_library.get_album_for_track(track_info.id)
                artwork = self.artwork_reader.get_artwork(file)
                if artwork is None:
                    artwork = self.local_folder_artwork_reader.get_artwork(album)
                if artwork is not None:
                    self.artwork_repository.save(album.id, artwork)

            except UnknownAudioFileFormatException:
                continue
