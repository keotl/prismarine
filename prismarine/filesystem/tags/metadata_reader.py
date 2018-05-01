import mutagen
from jivago.inject.registry import Component
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

from prismarine.media_info.track_info import TrackInfo


@Component
class MetadataReader(object):

    def read_metadata(self, file_path: str) -> TrackInfo:
        audio_file = mutagen.File(file_path)
        if isinstance(audio_file, MP3):
            return TrackInfo(None, audio_file['TIT2'].text[0], audio_file['TPE1'].text[0], audio_file.info.length,
                             'MP3', audio_file['TCON'],
                             int(audio_file['TRCK'].text[0].split('/')[0]),
                             int(audio_file['TRCK'].text[0].split('/')[1]))
        if isinstance(audio_file, FLAC):
            return TrackInfo(None, audio_file['title'][0], audio_file['artist'][0], audio_file.info.length,
                             'FLAC', audio_file['genre'][0], int(audio_file['tracknumber'][0]),
                             int(audio_file['totaltracks'][0]))
