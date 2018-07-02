import glob
import os

from jivago.lang.registry import Component

from prismarine.filesystem.tags.artwork import Artwork
from prismarine.media_info.album_info import AlbumInfo

picture_file_extensions = [('*.png', 'image/png'), ('*.jpg', 'image/jpeg'), ('*.jpeg', 'image/jpeg'),
                           ('*.bmp', 'image/bmp'), ('*.gif', 'image/gif')]


@Component
class LocalFolderArtworkReader(object):

    def get_artwork(self, album: AlbumInfo) -> Artwork:

        for extension, mime_type in picture_file_extensions:
            files = glob.glob(os.path.join(album.folder_path, extension))
            if len(files) > 0:
                with open(files[0], 'rb') as f:
                    return Artwork(mime_type, f.read())

        return None
