import requests
from jivago.lang.registry import Component

from prismarine.filesystem.media.artist_image_provider import ArtistImageProvider
from prismarine.filesystem.tags.artwork import Artwork

apiKey = '9b9a33c6e5554a996c2174a8c61b574a'
baseUrl = 'http://ws.audioscrobbler.com/2.0/?method='


@Component
class LastFmImageProvider(ArtistImageProvider):

    def get_artist_image(self, artist_name: str) -> Artwork:
        url = '{}artist.getinfo&artist={}&api_key={}&format=json'.format(baseUrl, artist_name, apiKey)
        try:
            response = requests.request("GET", url)
            artwork_url = response.json()['artist']['image'][4]['#text']
            artwork_data = requests.request("GET", artwork_url)
            return Artwork(artwork_data.headers['Content-Type'], artwork_data.content)
        except:
            print("exceeded lastfm call limit.")
            return None
