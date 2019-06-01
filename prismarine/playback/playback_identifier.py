import uuid


class PlaybackIdentifier(object):

    def __init__(self):
        self.id = uuid.uuid4()

    def __eq__(self, other):
        return isinstance(other, PlaybackIdentifier) and self.id == other.id
