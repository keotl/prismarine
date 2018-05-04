from typing import List

import mutagen
from jivago.inject.registry import Component
from jivago.lang.stream import Stream

from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.track_info import TrackInfo


@Component
class MetadataReader(object):
    def __init__(self, reading_strategies: List[MetadataReadingStrategy]):
        self.reading_strategies = reading_strategies

    def read_metadata(self, file_path: str) -> TrackInfo:
        audio_file = mutagen.File(file_path)
        metadata_reading_strategy: MetadataReadingStrategy = Stream(self.reading_strategies).firstMatch(
            lambda s: s.matches(audio_file))

        if metadata_reading_strategy is None:
            raise UnknownAudioFileFormatException()

        return TrackInfo(
            None,
            metadata_reading_strategy.get_title(audio_file),
            metadata_reading_strategy.get_artist(audio_file),
            metadata_reading_strategy.get_album(audio_file),
            metadata_reading_strategy.get_length(audio_file),
            metadata_reading_strategy.get_format(audio_file),
            metadata_reading_strategy.get_genre(audio_file),
            metadata_reading_strategy.get_track_number(audio_file),
            metadata_reading_strategy.get_total_tracks(audio_file)
        )



