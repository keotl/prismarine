import unittest
from unittest import mock

from prismarine.filesystem.tags.metadata_reader import MetadataReader
from prismarine.filesystem.tags.metadata_reading_strategy import MetadataReadingStrategy
from prismarine.filesystem.tags.unknown_audio_file_format_exception import UnknownAudioFileFormatException
from prismarine.media_info.track_info import TrackInfo

TITLE = "A Title"
LENGTH = 5550
ARTIST = "An Artist"
ALBUM = 'An Album'
GENRE = "A Friend"
TRACK_NUMBER = 1
TOTAL_TRACKS = 12

FILE = "../../../test-data/file-mp3.mp3"


class MetadataReaderTest(unittest.TestCase):

    def setUp(self):
        self.readerMock: MetadataReadingStrategy = mock.create_autospec(MetadataReadingStrategy)
        self.metadataReader = MetadataReader([self.readerMock])
        self.readerMock.matches.return_value = True
        self.readerMock.get_artist.return_value = ARTIST
        self.readerMock.get_title.return_value = TITLE
        self.readerMock.get_length.return_value = LENGTH
        self.readerMock.get_album.return_value = ALBUM
        self.readerMock.get_genre.return_value = GENRE
        self.readerMock.get_track_number.return_value = TRACK_NUMBER
        self.readerMock.get_total_tracks.return_value = TOTAL_TRACKS

    def test_whenReadingMetadata_thenCallMetadataReadingStrategy(self):
        track_info = self.metadataReader.read_metadata(FILE)

        self.assertMetadataIsCorrectlyLoaded(track_info)

    def test_givenNoMatchingMetadataReadingStrategy_whenReadingMetadata_thenThrowUnknownAudioFileFormatException(self):
        self.metadataReader = MetadataReader([])

        with self.assertRaises(UnknownAudioFileFormatException):
            self.metadataReader.read_metadata(FILE)

    def assertMetadataIsCorrectlyLoaded(self, track_info: TrackInfo):
        self.assertEqual(ARTIST, track_info.artist)
        self.assertEqual(TITLE, track_info.title)
        self.assertAlmostEqual(LENGTH, track_info.length, delta=0.01)
        self.assertEqual(TRACK_NUMBER, track_info.number)
        self.assertEqual(TOTAL_TRACKS, track_info.tracks_on_disc)
        self.assertEqual(ALBUM, track_info.album)
