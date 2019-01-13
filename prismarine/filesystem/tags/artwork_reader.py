from typing import List

import mutagen
from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream

from prismarine.filesystem.tags.artwork import Artwork
from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException


@Component
class ArtworkReader(object):

    @Inject
    def __init__(self, metadata_reading_strategies: List[MetadataReadingStrategy]):
        self.metadata_reading_strategies = metadata_reading_strategies

    def get_artwork(self, file_path: str) -> Artwork:
        audio_file = mutagen.File(file_path)

        strategy: MetadataReadingStrategy = Stream(self.metadata_reading_strategies).firstMatch(
            lambda s: s.matches(audio_file))
        if strategy is None:
            raise UnknownAudioFileFormatException()

        return strategy.get_cover_art(audio_file)
