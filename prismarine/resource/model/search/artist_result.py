from jivago.lang.annotations import Serializable


@Serializable
class ArtistResult(object):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
