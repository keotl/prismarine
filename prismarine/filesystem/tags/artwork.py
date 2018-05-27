class Artwork(object):

    def __init__(self, mime_type: str, content: bytes):
        self.mime_type = mime_type
        self.data = content
