import unittest

import mutagen
from mutagen import FileType

from prismarine.filesystem.tags.flac_metadata_reading_strategy import FlacMetadataReadingStrategy
from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy
from prismarine.filesystem.tags.mp3_metadata_reading_strategy import Mp3MetadataReadingStrategy

TITLE = "A Title"
LENGTH = 0.055425
ARTIST = "An Artist"
GENRE = "A Friend"
ALBUM = "An Album"
TRACK_NUMBER = 1
TOTAL_TRACKS = 12

MP3_FILE = "../../../test-data/file-mp3.mp3"
FLAC_FILE = "../../../test-data/file-flac.flac"


class MetadataReadingStrategyTest(unittest.TestCase):

    def test_readMp3File(self):
        strategy = Mp3MetadataReadingStrategy()
        audio_file = mutagen.File(MP3_FILE)

        self.assertStrategyReturnsCorrectMetadata(strategy, audio_file)

    def test_readFlacFile(self):
        strategy = FlacMetadataReadingStrategy()
        audio_file = mutagen.File(FLAC_FILE)

        self.assertStrategyReturnsCorrectMetadata(strategy, audio_file)

    def assertStrategyReturnsCorrectMetadata(self, strategy: MetadataReadingStrategy, file: FileType):
        self.assertEqual(ARTIST, strategy.get_artist(file), "artist")
        self.assertEqual(TITLE, strategy.get_title(file), "title")
        self.assertAlmostEqual(LENGTH, strategy.get_length(file), delta=0.01, msg="length")
        self.assertEqual(TRACK_NUMBER, strategy.get_track_number(file), "track number")
        self.assertEqual(TOTAL_TRACKS, strategy.get_total_tracks(file), "total tracks")
        self.assertEqual(ALBUM, strategy.get_album(file), "album")
