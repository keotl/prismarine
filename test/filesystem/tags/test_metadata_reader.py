import unittest

from prismarine.filesystem.tags.metadata_reader import MetadataReader
from prismarine.media_info.track_info import TrackInfo

TITLE = "A Title"
LENGTH = 0.055425
ARTIST = "An Artist"
GENRE = "A Friend"
TRACK_NUMBER = 1
TOTAL_TRACKS = 12

MP3_FILE = "../../../test-data/file-mp3.mp3"
FLAC_FILE = "../../../test-data/file-flac.flac"

class MetadataReaderTest(unittest.TestCase):

    def setUp(self):
        self.metadataReader = MetadataReader()

    def test_loadMp3Metadata(self):
        track_info = self.metadataReader.read_metadata(MP3_FILE)

        self.assertMetadataIsCorrectlyLoaded(track_info)

    def test_loadFlacMetadata(self):
        track_info = self.metadataReader.read_metadata(FLAC_FILE)

        self.assertMetadataIsCorrectlyLoaded(track_info)

    def assertMetadataIsCorrectlyLoaded(self, track_info: TrackInfo):
        self.assertEqual(ARTIST, track_info.artist)
        self.assertEqual(TITLE, track_info.title)
        self.assertAlmostEqual(LENGTH, track_info.length, delta=0.01)
        self.assertEqual(TRACK_NUMBER, track_info.number)
        self.assertEqual(TOTAL_TRACKS, track_info.tracks_on_disc)

