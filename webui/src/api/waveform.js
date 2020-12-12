import {
  waveformServer
} from '../config'

export function getAlbumInfo(albumId) {
  return fetch(`${waveformServer}/info/album/${albumId}`).then(res => res.json());
}

export function getTrackInfo(trackId) {
  return fetch(`${waveformServer}/info/track/${trackId}`).then(res => res.json());
}

export function getArtistInfo(artistId) {
  return fetch(`${waveformServer}/info/artist/${artistId}`).then(res => res.json());
}

export function searchTracks(query) {
  return fetch(`${waveformServer}/search/tracks?q=${query}`).then(res => res.json()).then(json => json.tracks);
}

export function searchAlbums(query) {
  return fetch(`${waveformServer}/search/albums?q=${query}`).then(res => res.json()).then(json => json.albums);
}

export function searchArtists(query) {
  return fetch(`${waveformServer}/search/artists?q=${query}`).then(res => res.json()).then(json => json.artists);
}

export function getArtistSummary() {
  return fetch(`${waveformServer}/summary/artists`).then(res => res.json()).then(json => json.artists);
}

export function getAlbumSummary() {
  return fetch(`${waveformServer}/summary/albums`).then(res => res.json()).then(json => json.albums);
}
