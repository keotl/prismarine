from datetime import datetime

from jivago.lang.annotations import Override
from jivago.lang.registry import Component
from mutagen import FileType
from mutagen.mp4 import MP4

from prismarine.filesystem.tags.artwork import Artwork
from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy


@Component
class Mp4MetadataReadingStrategy(MetadataReadingStrategy):

    @Override
    def matches(self, audio_file: FileType) -> bool:
        return isinstance(audio_file, MP4)

    @Override
    def get_artist(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, '©ART')

    @Override
    def get_album(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, '©alb')

    @Override
    def get_length(self, audio_file: FileType) -> float:
        return audio_file.info.length

    @Override
    def get_genre(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, '©gen')

    @Override
    def get_track_number(self, audio_file: FileType) -> int:
        try:
            return audio_file['trkn'][0][0]
        except:
            return None

    @Override
    def get_total_tracks(self, audio_file: FileType) -> int:
        try:
            return audio_file['trkn'][0][1]
        except:
            return None

    @Override
    def get_format(self, audio_file: FileType) -> str:
        return audio_file.info.codec_description

    @Override
    def get_title(self, audio_file: FileType) -> str:
        return self.get_or_none(audio_file, '©nam')

    @Override
    def get_cover_art(self, audio_file: FileType) -> Artwork:
        try:
            cover = audio_file['covr'][0]
            mime_type = 'image/jpeg' if cover.imageformat == cover.FORMAT_JPEG else 'image/png' if cover.imageformat == cover.FORMAT_PNG else ''
            if mime_type != '':
                return Artwork(mime_type, bytes(audio_file['covr'][0]))
        except:
            return None

    @Override
    def get_disc_number(self, audio_file: FileType) -> int:
        try:
            return audio_file['disc'][0][0]
        except:
            return None

    @Override
    def get_release_year(self, audio_file: FileType) -> int:
        try:
            day = audio_file['©day'][0]
            if day[:4].isdigit():
                return int(day[:4])
            return datetime.strptime(day, '%Y-%m-%dT%H:%M:%SZ').year
        except:
            return None
