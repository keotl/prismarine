from jivago.inject.registry import Component


@Component
class MetadataDefaultValues(object):
    id = None
    artist = 'Unknown Artist'
    album = 'Unknown Album'
    title = 'Unknown Track'
    genre = 'Other'
    track_number = 0
    total_tracks = 0
