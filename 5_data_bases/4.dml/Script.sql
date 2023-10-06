CREATE TABLE IF NOT EXISTS Genres(
	genre_id INT PRIMARY KEY,
	genre_name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists(
	artist_id INT PRIMARY KEY,
	artist_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenresArtists(
	genre_id INT REFERENCES Genres(genre_id),
	artist_id INT REFERENCES Artists(artist_id),
	CONSTRAINT pk_genres_artists PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS Albums(
	album_id INT PRIMARY KEY,
	album_name VARCHAR(200) NOT NULL,
	release_year INT NOT NULL
);

CREATE TABLE IF NOT EXISTS ArtistsAlbum(
	artist_id INT REFERENCES Artists(artist_id),
	album_id INT REFERENCES Albums(album_id),
	CONSTRAINT pk_artist_album PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS Tracks(
	track_id INT PRIMARY KEY,
	track_name VARCHAR(200) NOT NULL,
	track_length TIME,
	album_id INT REFERENCES Albums(album_id)
);

CREATE TABLE IF NOT EXISTS Collection(
	collection_id INT PRIMARY KEY,
	collection_name VARCHAR(200) NOT NULL,
	release_year INT NOT NULL
);

CREATE TABLE IF NOT EXISTS TracksCollections(
	track_id INT REFERENCES Tracks(track_id),
	collection_id INT REFERENCES Collection(collection_id),
	CONSTRAINT pk_tracks_collections PRIMARY KEY (track_id, collection_id)
);