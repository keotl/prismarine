const BASE_URL = process.env.REACT_APP_API_URL || "";
// const BASE_URL = "http://192.168.1.137:4000"
export type AlbumSummary = {
  id: string;
  artist: string;
  name: string;
  date: number;
  artwork_url: string;
};
export function listAlbums(): Promise<{ albums: AlbumSummary[] }> {
  return fetch(`${BASE_URL}/summary/albums`).then((r) => r.json());
}

export type Track = {
  id: string;
  album: string;
  album_id: string;
  artist: string;
  artwork_url: string;
  disc_number: string;
  genre: string;
  length: number;
  title: string;
  track_number: string;
};

export type Album = {
  id: string;
  artist: string;
  artist_id: string;
  artwork_url: string;
  genre: string;
  name: string;
  year: number;
  tracks: Track[];
};

export function getAlbum(albumId: string): Promise<Album> {
  return fetch(`${BASE_URL}/info/album/${albumId}`).then((r) => r.json());
}

export function trackUrl(trackId: string): string {
  return `${BASE_URL}/media/track/${trackId}`;
}

export function fetchArtwork(artwork_url: string): Promise<Blob | null> {
  if (!artwork_url) {
    return Promise.resolve(null);
  }
  return fetch(`${BASE_URL}${artwork_url}`).then((r) => r.blob());
}
