from mutagen import FileType

from prismarine.filesystem.tags.artwork import Artwork


class MetadataReadingStrategy(object):

    def matches(self, audio_file: FileType) -> bool:
        raise NotImplementedError

    def get_artist(self, audio_file: FileType) -> str:
        raise NotImplementedError

    def get_album(self, audio_file: FileType) -> str:
        raise NotImplementedError

    def get_length(self, audio_file: FileType) -> float:
        raise NotImplementedError

    def get_genre(self, audio_file: FileType) -> str:
        raise NotImplementedError

    def get_track_number(self, audio_file: FileType) -> int:
        raise NotImplementedError

    def get_total_tracks(self, audio_file: FileType) -> int:
        raise NotImplementedError

    def get_format(self, audio_file: FileType) -> str:
        raise NotImplementedError

    def get_title(self, audio_file: FileType) -> str:
        raise NotImplementedError

    def get_cover_art(self, audio_file: FileType) -> Artwork:
        raise NotImplementedError

    def get_disc_number(self, audio_file: FileType) -> int:
        raise NotImplementedError

    def get_release_year(self, audio_file: FileType) -> int:
        raise NotImplementedError

    def get_or_none(self, audio_file: FileType, key: str) -> str:
        return audio_file.get(key)[0] if audio_file.get(key) else None

    def get_numeric_or_none(self, audio_file: FileType, key: str) -> int:
        return int(audio_file.get(key)[0]) if audio_file.get(key) else None
