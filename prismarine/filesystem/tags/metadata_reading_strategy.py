from mutagen import FileType


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
