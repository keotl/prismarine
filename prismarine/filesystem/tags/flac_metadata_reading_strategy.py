from jivago.inject.registry import Component
from jivago.lang.annotations import Override
from mutagen import FileType
from mutagen.flac import FLAC

from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy


@Component
class FlacMetadataReadingStrategy(MetadataReadingStrategy):

    @Override
    def matches(self, audio_file: FileType) -> bool:
        return isinstance(audio_file, FLAC)

    @Override
    def get_artist(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, 'artist')

    @Override
    def get_album(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, 'album')

    @Override
    def get_length(self, audio_file: FileType) -> float:
        return audio_file.info.length

    @Override
    def get_genre(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, 'genre')

    @Override
    def get_track_number(self, audio_file: FileType) -> int:
        return self.get_numeric_or_none(audio_file, 'tracknumber')

    @Override
    def get_total_tracks(self, audio_file: FileType) -> int:
        return self.get_numeric_or_none(audio_file, 'totaltracks')

    @Override
    def get_format(self, audio_file: FileType) -> str:
        return 'FLAC'

    @Override
    def get_title(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, 'title')

    def get_or_none(self, audio_file: FileType, key: str) -> str:
        return audio_file.get(key)[0] if audio_file.get(key) else None

    def get_numeric_or_none(self, audio_file: FileType, key: str) -> int:
        return int(audio_file.get(key)[0]) if audio_file.get(key) else None
