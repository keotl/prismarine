import glob
import os

from jivago.lang.annotations import Inject
from jivago.lang.registry import Component
from jivago.lang.stream import Stream

from prismarine.filesystem.tags.metadata_reader import MetadataReader
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.media_library import MediaLibrary


@Component
class MediaIndexer(object):

    @Inject
    def __init__(self, media_library: MediaLibrary, metadata_reader: MetadataReader):
        self.metadata_reader = metadata_reader
        self.media_repository = media_library

    def index_tracks(self, folder_path: str):
        files = Stream(glob.glob(os.path.join(folder_path, '**/*'), recursive=True)).filter(
            lambda path: os.path.isfile(path)).toList()

        for file in files:
            try:
                track_info = self.metadata_reader.read_metadata(file)
                self.media_repository.save_track(track_info)
            except UnknownAudioFileFormatException:
                continue
