The classes I have chosen to create for this assignment implement Spotify functionality. This includes songs, users, albums, radios and playlists and the functionalities that come with these features.

## Songs

Song objects have the following attributes:

- Title
- Artist
- Album
- Genre
- Duration
- Release Date

Songs have the following methods:

- Play

## Playlists

Playlists have the following attributes:

- Title
- Author

and contain an internal list ‘songs’ which is a list composed of Song objects

Playlists have the following methods:

- Add to Playlist
- Remove from Playlist

## Users

Users have the following attributes:

- Username

Users have the following methods:

- Like Song
- Add playlist

## Album

The album inherits the base functionality of the Playlist as it is simply a playlist restrained to a certain artist and release date, and hence inherits all the properties from the Playlist.

With an additional attribute ‘artist’.

The Add To Album method overwrites the Add To Playlist method and requires the song to be from the same artist as the artist of the Album.

## Radio

The radio also inherits the base functionality of the Playlist but is restrained to a certain genre, while also inheriting all the properties from the Playlist.

The method Add to Radio requires the song to be of the same genre as the rest of the radio.