from prismarine.filesystem.tags.artwork import Artwork


class ArtistImageProvider(object):

    def get_artist_image(self, artist_name: str) -> Artwork:
        raise NotImplementedError
