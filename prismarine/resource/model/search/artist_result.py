from jivago.lang.annotations import Serializable


@Serializable
class ArtistResult(object):

    def __init__(self, id: str, name: str, artwork_url: str):
        self.artwork_url = artwork_url
        self.id = id
        self.name = name
