from typing import List

import mutagen
from jivago.inject.annotation import Component
from jivago.lang.annotations import Inject
from jivago.lang.stream import Stream

from prismarine.filesystem.tags.metadata_default_values import MetadataDefaultValues
from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.track_info import TrackInfo


@Component
class MetadataReader(object):

    @Inject
    def __init__(self, reading_strategies: List[MetadataReadingStrategy],
                 metadata_default_values: MetadataDefaultValues):
        self.metadata_default_values = metadata_default_values
        self.reading_strategies = reading_strategies

    def read_metadata(self, file_path: str) -> TrackInfo:
        audio_file = mutagen.File(file_path)

        metadata_reading_strategy: MetadataReadingStrategy = Stream(self.reading_strategies).firstMatch(
            lambda s: s.matches(audio_file))

        if metadata_reading_strategy is None:
            raise UnknownAudioFileFormatException()

        track_attributes = Stream({
                                      "id": None,
                                      "title": metadata_reading_strategy.get_title(audio_file),
                                      "artist": metadata_reading_strategy.get_artist(audio_file),
                                      "album": metadata_reading_strategy.get_album(audio_file),
                                      "length": metadata_reading_strategy.get_length(audio_file),
                                      "format": metadata_reading_strategy.get_format(audio_file),
                                      "genre": metadata_reading_strategy.get_genre(audio_file),
                                      "track_number": metadata_reading_strategy.get_track_number(audio_file),
                                      "total_tracks": metadata_reading_strategy.get_total_tracks(audio_file),
                                      "filename": audio_file.filename,
                                      "disc_number": metadata_reading_strategy.get_disc_number(audio_file),
                                      "release_year": metadata_reading_strategy.get_release_year(audio_file)
                                  }
                                  .items()).map(lambda k, v: (k, v if v else self._default_value(k))).toDict()
        return TrackInfo(**track_attributes)

    def _default_value(self, attribute_name: str):
        return self.metadata_default_values.__getattribute__(attribute_name)
