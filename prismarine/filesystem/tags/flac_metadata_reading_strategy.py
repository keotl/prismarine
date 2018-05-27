from jivago.lang.annotations import Override
from jivago.lang.registry import Component
from mutagen import FileType
from mutagen.flac import FLAC

from prismarine.filesystem.tags.artwork import Artwork
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

    @Override
    def get_cover_art(self, audio_file: FileType) -> Artwork:
        if len(audio_file.pictures) > 0:
            return Artwork(audio_file.pictures[0].mime, audio_file.pictures[0].data)
        return None

    @Override
    def get_release_year(self, audio_file: FileType) -> int:
        return self.get_numeric_or_none(audio_file, "date")

    @Override
    def get_disc_number(self, audio_file: FileType) -> int:
        return self.get_numeric_or_none(audio_file, "discnumber")
