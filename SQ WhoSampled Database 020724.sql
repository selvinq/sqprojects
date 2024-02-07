/*

Created by Selvin Quire
Date: 7/28/2023
Last Update: 2/7/2024
Description: This is the code to create the WhoSampled database.
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
	genre_name	varchar(50) NOT NULL,
	active		boolean NOT NULL
);

-- Update genre_name with a UNIQUE constraint.

ALTER TABLE whosampled.genre
ADD CONSTRAINT genre_name_key unique (genre_name);

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
		('Denied', 'Y')
;

-- Review the sub_decision table.

SELECT * FROM whosampled.sub_decision;

-- Create the US states table.

CREATE TABLE IF NOT EXISTS whosampled.us_states (
	state_id  	int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,	
	state		char(2) NOT NULL UNIQUE,
	state_name	varchar(50) NOT NULL UNIQUE
);

-- Insert data into states table

INSERT INTO whosampled.us_states (state, state_name)
VALUES ('DC','District of Columbia'),
('AL','Alabama'),
('AK','Alaska'),
('AZ','Arizona'),
('AR','Arkansas'),
('CA','California'),
('CO','Colorado'),
('CT','Connecticut'),
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
	state		char(2),
	country		varchar(80) NOT NULL
);

-- Add foreign key constraint to artist table to refer to us_states table.

ALTER TABLE music.artist ADD CONSTRAINT fk_states FOREIGN KEY (state) REFERENCES whosampled.us_states (state);

-- Test added foreign key constraint

INSERT INTO music.artist (artist_name, city, state, country)
VALUES 	('D''Angelo', 'Richmond', 'VB', 'United States');

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

-- Create the song type table. This will contain the types of samples that exist.

CREATE TABLE IF NOT EXISTS music.song_type (
	type_id		int2 PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	type_name	varchar(25) NOT NULL UNIQUE
);

-- Insert data into music.song_type table. These were pulled from the WhoSampled website.

INSERT INTO music.song_type (type_name)
VALUES	('Direct Sample'),
		('Interpolation'),
		('Cover'),
		('Remix'),
		('Fact / Story')
;

-- Review song type table.

SELECT * FROM music.song_type;


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

-- Inster data into the composer table.

INSERT INTO music.composer (composer_name, city, state, country)
VALUES 	('Sounwave', 'Compton', 'CA', 'United States'),
		('9th Wonder', 'Winston-Salem', 'NC', 'United States'),
		('D''Angelo', 'Richmond', 'VA', 'United States'),
		('Kanye West', 'Chicago', 'IL', 'United States'),
		('Kaytranda', 'Port-au-Prince', NULL, 'Haiti')
;

-- Review the composer table.

SELECT * FROM music.composer;