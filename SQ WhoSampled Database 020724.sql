/*

Created by Selvin Quire
Date: 7/28/2023
Last Update: 4/7/2024
Description: This is the code to replicate the WhoSampled.com database.
The syntax is based on the PostgreSQL database and documentation.

*/

-- Create the database.

CREATE DATABASE whosampled;

-- Create the schemas for the whosampled database.

CREATE SCHEMA music;
CREATE SCHEMA media;
CREATE SCHEMA members;
CREATE SCHEMA whosampled;


/* This section will create the parent tables in the WHOSAMPLED schema.
 * These tables will have relationships with all of the other schemas.*/

-- Create the genre table. This will contain all of the genres for each music, TV, and film entry.

CREATE TABLE IF NOT EXISTS whosampled.genre (
	genre_id	int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	genre_name	varchar(50) NOT NULL UNIQUE,
	active		boolean NOT NULL
);

-- Update genre_name with a UNIQUE constraint.

--ALTER TABLE whosampled.genre
--ADD CONSTRAINT genre_name_key unique (genre_name);

-- Insert data into the genre table (may not contain full list of genres from website).

INSERT INTO whosampled.genre (genre_name, active)
VALUES 	('Soul / Funk / Disco', 'Y'),
		('Hip-Hop / Rap / R&B', 'Y'),
		('Electronic / Dance', 'Y'),
		('Rock / Pop', 'Y'),
		('Jazz / Blues', 'Y'),
		('Country / Folk', 'Y'),
		('World / Latin', 'Y'),
		('Soundtrack / Latin', 'Y'),
		('Reggae / Dub', 'Y'),
		('Classical', 'Y'),
		('Spoken Word', 'Y'),
		('Easy Listening', 'Y'),
		('Gospel', 'Y'),
		('Other', 'Y'),
		('Action / Adventure', 'Y'),
		('Adventure', 'Y'),
		('Comedy', 'Y'),
		('Drama', 'Y'),
		('Thriller', 'Y'),
		('Horror', 'Y'),
		('Romance', 'Y'),
		('Anime / Animation', 'Y'),
		('Family', 'Y'),
		('Fantasy', 'Y'),
		('Sci-Fi', 'Y'),
		('Biography / History', 'Y')
;

-- Review the genre table.

SELECT * FROM whosampled.genre;

-- Create the element table. This will contain the types of elements that can be sampled from music, TV, or film.

CREATE TABLE IF NOT EXISTS whosampled.element (
	element_id		int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	element_name	varchar(50) NOT NULL UNIQUE,
	active			boolean NOT NULL
);

-- Insert data into the element table. These were pulled from the WhoSampled website.

INSERT INTO whosampled.element (element_name, active)
VALUES	('Multiple Elements', 'Y'),
		('Drums', 'Y'),
		('Bass', 'Y'),
		('Vocals / Lyrics', 'Y'),
		('Hook / Riff', 'Y'),
		('Sound Effect / Other', 'Y'),
		('Dialogue', 'Y'),
		('Score', 'Y')
;

-- Review the element table.

SELECT * FROM whosampled.element;

-- Create submission decision table. This will contain the decisions that can be made on an entry submission.

CREATE TABLE IF NOT EXISTS whosampled.sub_decision (
	decision_id		int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	decision_name	varchar(25) NOT NULL UNIQUE,
	active			boolean NOT NULL
);

-- Insert data into the sub_decision table.

INSERT INTO whosampled.sub_decision (decision_name, active)
VALUES	('Approved', 'Y'),
		('Denied', 'Y'),
		('Pending', 'Y')
;

-- Review the sub_decision table.

SELECT * FROM whosampled.sub_decision;

-- Create the US states table. The table will also include US territories.

CREATE TABLE IF NOT EXISTS whosampled.us_states (
	state_id  	int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,	
	state		char(2) NOT NULL UNIQUE,
	state_name	varchar(50) NOT NULL UNIQUE
);

-- Insert data into states table

INSERT INTO whosampled.us_states (state, state_name)
VALUES 
('AL','Alabama'),
('AK','Alaska'),
('AZ','Arizona'),
('AR','Arkansas'),
('CA','California'),
('CO','Colorado'),
('CT','Connecticut'),
('DC','District of Columbia'),
('DE','Delaware'),
('FL','Florida'),
('GA','Georgia'),
('HI','Hawaii'),
('ID','Idaho'),
('IL','Illinois'),
('IN','Indiana'),
('IA','Iowa'),
('KS','Kansas'),
('KY','Kentucky'),
('LA','Louisiana'),
('ME','Maine'),
('MD','Maryland'),
('MA','Massachusetts'),
('MI','Michigan'),
('MN','Minnesota'),
('MS','Mississippi'),
('MO','Missouri'),
('MT','Montana'),
('NE','Nebraska'),
('NV','Nevada'),
('NH','New Hampshire'),
('NJ','New Jersey'),
('NM','New Mexico'),
('NY','New York'),
('NC','North Carolina'),
('ND','North Dakota'),
('OH','Ohio'),
('OK','Oklahoma'),
('OR','Oregon'),
('PA','Pennsylvania'),
('RI','Rhode Island'),
('SC','South Carolina'),
('SD','South Dakota'),
('TN','Tennessee'),
('TX','Texas'),
('UT','Utah'),
('VT','Vermont'),
('VA','Virginia'),
('WA','Washington'),
('WV','West Virginia'),
('WI','Wisconsin'),
('WY','Wyoming'),
('AS','American Samoa'),
('FM','Federated States of Micronesia'),
('GU','Guam'),
('MH','Marshall Islands'),
('MP','Northern Mariana Islands'),
('PR','Puerto Rico'),
('PW','Palau'),
('VI','U.S. Virgin Islands')
;

-- Review the us_states table.

SELECT * FROM whosampled.us_states;




/* The following section will list the codes to create the parent and child tables for the MUSIC schema.*/


-- PARENT TABLES


-- Creating the artist table. This will contain the music artists in the database.

CREATE TABLE IF NOT EXISTS music.artist (
	artist_id 	int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	artist_name varchar(80) NOT NULL UNIQUE,
	city		varchar(80) NOT NULL,
	state		char(2) REFERENCES whosampled.us_states (state),
	country		varchar(80) NOT NULL
);


-- Insert data into the artist table.

INSERT INTO music.artist (artist_name, city, state, country)
VALUES 	('D''Angelo', 'Richmond', 'VA', 'United States'),
		('Kanye West', 'Chicago', 'IL', 'United States'),
		('Kaytranda', 'Port-au-Prince', NULL, 'Haiti'),
		('Kendrick Lamar', 'Compton', 'CA', 'United States'),
		('Little Brother', 'Durham', 'NC', 'United States')
;

-- Review the artist table.

SELECT * FROM music.artist;

-- Create the song type table that will contain the types of songs that exist.

CREATE TABLE IF NOT EXISTS whosampled.music.song_type (
	type_id		int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	type_name	varchar(25) NOT NULL UNIQUE
);

INSERT INTO whosampled.music.song_type (type_name)
VALUES 	('Original'),
		('Remix'),
		('Cover')
;


-- Review song type table.

SELECT * FROM music.song_type;


-- Create the sample type table. This will contain the types of samples that exist.

CREATE TABLE IF NOT EXISTS whosampled.music.sample_type (
	type_id		int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	type_name	varchar(25) NOT NULL UNIQUE
);



-- Insert data into music.sample_type table. These were pulled from the WhoSampled website.

INSERT INTO whosampled.music.sample_type (type_name)
VALUES	('Direct Sample'),
		('Interpolation'),
		('Cover'),
		('Remix'),
		('Fact / Story')
;

-- Review sample type table.

SELECT * FROM music.sample_type;


-- Create the label table. This will contain the music labels that artists are signed to at time of their song releases.

CREATE TABLE IF NOT EXISTS music.music_label (
	label_id	int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	label_name	varchar(50) NOT NULL
);

-- Insert sample data into music.label table

INSERT INTO music.music_label (label_name)
VALUES	('ABB'),
		('EMI'),
		('XL'),
		('Roc-A-Fella'),
		('Top Dawg Entertainment');

-- Review music.label table

SELECT * FROM music.music_label;

-- Create the composer table. This will contain the music producers in the database.


CREATE TABLE IF NOT EXISTS music.composer (
	composer_id		int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	composer_name	varchar(80) NOT NULL UNIQUE,
	city			varchar(80) NOT NULL,
	state			char(2) REFERENCES whosampled.us_states(state),
	country			varchar(80) NOT NULL
);

-- Insert data into the composer table.

INSERT INTO music.composer (composer_name, city, state, country)
VALUES 	('Sounwave', 'Compton', 'CA', 'United States'),
		('9th Wonder', 'Winston-Salem', 'NC', 'United States'),
		('D''Angelo', 'Richmond', 'VA', 'United States'),
		('Kanye West', 'Chicago', 'IL', 'United States'),
		('Kaytranda', 'Port-au-Prince', NULL, 'Haiti')
;

-- Review the composer table.

SELECT * FROM music.composer;













-- Create the parent tables for the MEMBERS schema.


CREATE TABLE IF NOT EXISTS members.contributor (
	contributor_id	int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	email			varchar(80) NOT NULL UNIQUE,
	username		varchar(80) NOT NULL UNIQUE,
	password		varchar(80) NOT NULL
);

-- Inserting sample data to the members.contributor table

INSERT INTO whosampled.members.contributor (email, username, password)
VALUES
	('emailaddress1@gmail.com', 'user111', '123456'),
	('emailaddress2@yahoo.com', 'user222', '123456'),
	('emailaddress3@aol.com', 'user333', '123456'),
	('emailaddress4@hotmail.com', 'user444', '123456'),
	('emailaddress5@icloud.com', 'user555', '123456')
;

/* The following section will list the codes to create the CHILD tables for each schema.*/

-- Create the child tables for the MUSIC schema.

CREATE TABLE IF NOT EXISTS music.album (
	album_id	int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	album_name	varchar(80) NOT NULL,
	artist_id	int4 NOT NULL REFERENCES music.artist(artist_id),
	release_year int2 CHECK (release_year >= 0 AND release_year <= 2030)
);

-- Add sample data to album table


INSERT INTO music.album (album_name, artist_id)
VALUES 	('The College Dropout', 6, 2004),
		('99.9%', 7, 2016),
		('Brown Sugar', 5, 1995),
		('Section.80', 8, 2011),
		('The Listening', 9, 2003)
;

-- Review album table

SELECT * FROM whosampled.music.album;

-- Create the song table. This will serve as the master song table.


CREATE TABLE IF NOT EXISTS whosampled.music.song (
	song_id			int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	song_name		varchar(80) NOT NULL,
	artist_id		int4 NOT NULL REFERENCES music.artist(artist_id),
	genre_id		int2 NOT NULL REFERENCES whosampled.genre(genre_id),
	album_id		int4 REFERENCES music.album(album_id),
	song_type_id	int2 NOT NULL REFERENCES music.song_type(type_id),
	bpm				int2 CHECK (bpm > 0),
	label_id		int4 NOT NULL REFERENCES music.music_label(label_id),
	release_year	int2 NOT NULL CHECK (release_year >= 0 AND release_year <= 2030),
	track_number 	int2 NOT NULL,
	song_key 		varchar(10)
);

-- Create an Original Song table will contain copies of the records from select columns of the Song table.
-- This will serve as a reference table, separate from the Song table, when comparing sampling and original songs.

CREATE TABLE IF NOT EXISTS whosampled.music.original_song (
	song_id			int4 PRIMARY KEY,
	song_name		varchar(80) NOT NULL,
	artist_id		int4 NOT NULL REFERENCES music.artist(artist_id),
	album_id		int4 REFERENCES music.album(album_id)
);

-- Insert data into the Song table

INSERT INTO whosampled.music.song
(song_name, artist_id, genre_id, album_id, song_type_id, bpm, label_id, release_year, track_number, song_key)
VALUES (
	'Through the Wire',
	6,
	3,
	1,
	1,
	83,
	4,
	2002,
	19,
	'G'
)
;

SELECT * FROM whosampled.music.song;

-- Copy data from the Song table to the Original Song table

INSERT INTO whosampled.music.original_song (song_id, song_name, artist_id, album_id)
SELECT
	song_id,
	song_name,
	artist_id,
	album_id
FROM
	whosampled.music.song
WHERE
	song_id NOT IN (SELECT song_id FROM whosampled.music.original_song)
;

SELECT * FROM whosampled.music.original_song;
-- FACT TABLE

CREATE TABLE IF NOT EXISTS music.music_sub (
	music_sub_id		int4 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	submission_date		timestamp NOT NULL DEFAULT NOW(),
	contributor_id		int4 NOT NULL REFERENCES members.contributor(contributor_id),
	sample_type_id		int2 NOT NULL REFERENCES music.sample_type(type_id),
	element_id			int2 NOT NULL REFERENCES whosampled.element(element_id),
	s_artist_id			int4 NOT NULL REFERENCES music.artist(artist_id), -- "s" = sampling song
	s_song_id			int4 NOT NULL REFERENCES music.song(song_id),
	s_sample_appears	int4 NOT NULL CHECK (s_sample_appears >= 0), -- recorded in seconds
	s_throughout		boolean NOT NULL,
	s_album_id			int4 REFERENCES music.album(album_id),
	s_label_id			int4 NOT NULL REFERENCES music.music_label(label_id),
	s_year				int2 NOT NULL CHECK (s_year BETWEEN 0 AND 2030),
	s_genre_id			int2 NOT NULL REFERENCES whosampled.genre(genre_id),
	s_track_image		bytea NOT NULL,
	s_video_embed		varchar(80) NOT NULL, -- video link (i.e. YouTube)
	o_artist_id			int4 NOT NULL REFERENCES music.artist(artist_id), -- "o" = original (sampled) song
	o_song_id			int4 NOT NULL REFERENCES music.song(song_id),
	o_sample_appears	int4 NOT NULL CHECK (o_sample_appears >= 0), -- recorded in seconds
	o_album_id			int4 REFERENCES music.album(album_id),
	o_label_id			int4 NOT NULL REFERENCES music.music_label(label_id),
	o_year				int2 NOT NULL CHECK (s_year BETWEEN 0 AND 2030),
	o_genre_id			int2 NOT NULL REFERENCES whosampled.genre(genre_id),
	o_track_image		bytea NOT NULL,
	o_video_embed		varchar(80) NOT NULL,
	decision_id			int2 NOT NULL REFERENCES whosampled.sub_decision DEFAULT 3 --pending status as default
);


/* 
  
 Create a view of the music submissions table that shows the approved submissions.

 */


CREATE VIEW final_music_samples AS
	SELECT
		ms.music_sub_id AS SampleID,
		s_artist_id AS SamplingArtistID,
		s_song_id AS SamplingSong,
		s_album_id AS Album1,
		s_year AS Released1,
		s_genre_id AS GenreID1,
		o_artist_id AS OriginalArtist,
		o_song_id AS OriginalSong,
		o_album_id AS Album2,
		o_label_id AS Label2,
		o_year AS Released2,
		o_genre_id AS GenreID2,
		sample_type_id AS SampleType,
		element_id AS ElementID
	FROM
		music.music_sub ms
	where
		decision_id = 1
;

SELECT * FROM final_music_samples;



/* This section will build data into the tables that will create sample submissions
 * Kanye West's "Through the Wire" and "All Falls Down" will be used to create the submissions.*/



-- Inserting more data into the music.artist table

INSERT INTO whosampled.music.artist (artist_name, city, state, country)
VALUES
	('Chaka Khan', 'Chicago', 'IL', 'United States'),
	('OutKast', 'Atlanta', 'GA', 'United States'),
	('Linda Kaplan Thaler', 'New York', 'NY', 'United States'),
	('Lauryn Hill', 'East Orange', 'NJ', 'United States'),
	('The Notorious B.I.G.', 'Brooklyn', 'NY', 'United States')
;

-- Inserting data into the music.music.label table based on the artists and their sampled songs above

INSERT INTO whosampled.music.music_label (label_name)
VALUES
	('Warner Bros.'),
	('LaFace'),
	('Toys ''R'' Us'),
	('Columbia'),
	('Bad Boy'),
	('Chi Town Gettin Down')
;

-- Inserting data into the music.album table based on the artists and their sampled songs

INSERT INTO whosampled.music.album (album_name, artist_id, release_year)
VALUES
	('I Feel For You', 10, 1984),
	('Player''s Ball', 11, 1993),
	('I Don''t Wanna Grow Up, I''m a Toys ''R'' Us Kid', 12, 1980),
	('MTV Unplugged 2.0', 13, 2002),
	('Unreleased & Unleashed', 14, 1995),
	('Freshmen Adjustment', 6, 2004)
;


-- Adding songs from The College Dropout to the song table

INSERT INTO whosampled.music.song (song_name, artist_id, genre_id, album_id, song_type_id, bpm, label_id, release_year, track_number, song_key)
VALUES
	('Intro', 6, 3, 1, 1, NULL, 4, 2002, 1, NULL),
	('We Don''t Care', 6, 3, 1, 1, 83, 4, 2002, 2, 'D'),
	('Graduation Day', 6, 3, 1, 1, NULL, 4, 2002, 3, NULL),
	('All Falls Down', 6, 3, 1, 1, 91, 4, 2002, 4, 'G#/Ab'),
	('I''ll Fly Away', 6, 3, 1, 1, 172, 4, 2002, 5, 'F#/Gb'),
	('Spaceship', 6, 3, 1, 1, 178, 4, 2002, 6, 'F'),
	('Jesus Walks', 6, 3, 1, 1, 87, 4, 2002, 7, 'D#/Eb'),
	('Never Let Me Down', 6, 3, 1, 1, 80, 4, 2002, 8, 'B'),
	('Get Em High', 6, 3, 1, 1, 85, 4, 2002, 9, 'B'),
	('Workout Plan', 6, 3, 1, 1, NULL, 4, 2002, 10, NULL),
	('The New Workout Plan', 6, 3, 1, 1, 118, 4, 2002, 11, 'D'),
	('Slow Jamz', 6, 3, 1, 1, 145, 4, 2002, 12, 'D'),
	('Breathe In Breathe Out', 6, 3, 1, 1, 89, 4, 2002, 13, 'C#/Db'),
	('School Spirit (Skit 1)', 6, 3, 1, 1, NULL, 4, 2002, 14, NULL),
	('School Spirit', 6, 3, 1, 1, 85, 4, 2002, 15, 'F'),
	('School Spirit (Skit 2)', 6, 3, 1, 1, NULL, 4, 2002, 16, NULL),
	('Lil Jimmy', 6, 3, 1, 1, NULL, 4, 2002, 17, NULL),
	('Two Words', 6, 3, 1, 1, 85, 4, 2002, 18, 'F#/Gb'),
	('Family Business', 6, 3, 1, 1, 94, 4, 2002, 20, 'C#/Db'),
	('Last Call', 6, 3, 1, 1, 83, 4, 2002, 21, 'G#/Ab')
;

-- Adding Chaka Khan's "Through the Fire" to the song table for the submission sampled data.

INSERT INTO music.song (song_name, artist_id, genre_id, album_id, song_type_id, bpm, label_id, release_year, track_number, song_key)
VALUES ('Through The Fire', 10, 3, 6, 1, 131, 6, 1984, 8, 'G#/Ab')
;

-- Adding sample submission data

INSERT INTO music.music_sub (
	contributor_id,
	sample_type_id,
	element_id,
	s_artist_id,
	s_song_id,
	s_sample_appears,
	s_throughout,
	s_album_id,
	s_label_id,
	s_year,
	s_genre_id,
	s_track_image,
	s_video_embed,
	o_artist_id,
	o_song_id,
	o_sample_appears,
	o_album_id,
	o_label_id,
	o_year,
	o_genre_id,
	o_track_image,
	o_video_embed
)
VALUES (1, 1, 1, 6, 1, 0, TRUE, 1, 4, 2002, 3, NULL, 'https://youtu.be/AE8y25CcE6s', 10, 22, 191, 6, 6, 1984, 3, NULL, 'https://youtu.be/TjWmw-8-OEk')
;


-- 2nd attempt to add submission data was successful after dropped constraint.

/*Testing the final music samples view.
 * The view should appear blank as the sample submission is still in a pending status.
 */

SELECT * FROM final_music_samples;

-- No results as expected

-- Simulating an approved submission by updating the decision ID on the sample record.

UPDATE music.music_sub
SET decision_id = 1
WHERE music.music_sub.music_sub_id = 2
;


SELECT * FROM final_music_samples;



/* This section contains a series of additional views that would likely be used to analyze data in the database.
 * Album/Artist
 * Sampled Song/Original Song
 * Most Contributions
 * */

-- VIEW #1: ALBUM & ARTIST

CREATE VIEW album_artist AS (
	SELECT
		ar.artist_name AS Artist,
		al.album_name AS Album,
		al.release_year AS Release_Year
	FROM
		whosampled.music.artist ar
	JOIN
		whosampled.music.album al
	ON
		ar.artist_id = al.artist_id
)
;

SELECT * FROM album_artist;

-- VIEW #2: ALBUM TRACKLIST

CREATE VIEW album_tracklist AS (
	SELECT
		s.track_number AS Track_Number,
		s.song_name AS Song_Name,
		al.album_name AS Album_Name
	FROM
		whosampled.music.song s
	JOIN	
		whosampled.music.album al
	ON
		s.album_id = al.album_id
	ORDER BY
		Track_Number
)
;

SELECT * FROM album_tracklist WHERE Album_Name = 'The College Dropout';
