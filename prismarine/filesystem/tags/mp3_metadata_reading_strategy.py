from jivago.lang.annotations import Override
from jivago.lang.registry import Component
from mutagen import FileType
from mutagen.mp3 import MP3

from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy


@Component
class Mp3MetadataReadingStrategy(MetadataReadingStrategy):

    @Override
    def matches(self, audio_file: FileType) -> bool:
        return isinstance(audio_file, MP3)

    @Override
    def get_artist(self, audio_file: FileType) -> str:
        return audio_file['TPE1'].text[0]

    @Override
    def get_album(self, audio_file: FileType) -> str:
        return audio_file['TALB'].text[0]

    @Override
    def get_length(self, audio_file: FileType) -> float:
        return audio_file.info.length

    @Override
    def get_genre(self, audio_file: FileType) -> str:
        return audio_file['TCON']

    @Override
    def get_track_number(self, audio_file: FileType) -> int:
        return int(audio_file['TRCK'].text[0].split('/')[0])

    @Override
    def get_total_tracks(self, audio_file: FileType) -> int:
        return int(audio_file['TRCK'].text[0].split('/')[1])

    @Override
    def get_format(self, audio_file: FileType) -> str:
        return 'MP3'

    @Override
    def get_title(self, audio_file: FileType) -> str:
        return audio_file['TIT2'].text[0]
