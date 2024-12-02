CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE content.genre (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    target_audience VARCHAR(10) CHECK (target_audience IN ('Kids', 'Teenagers', 'Adult')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE content.actor (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    birth_date DATE NOT NULL,
    birth_city VARCHAR(100) NOT NULL,
    birth_county VARCHAR(100) NOT NULL,
    short_bio TEXT,
    role VARCHAR(50) NOT NULL,
    nationality VARCHAR(50),
    gender VARCHAR(6) CHECK (gender IN ('female', 'male')),
    photo VARCHAR(255),
    start_year INTEGER NOT NULL,
    end_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE content.filmwork (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    data_release DATE NOT NULL,
    duration_min INTEGER NOT NULL,
    rating DECIMAL(3,1) DEFAULT 1 CHECK (rating >= 0 AND rating <= 10),
    age_limit VARCHAR(4) CHECK (age_limit IN ('7+', '12+', '16+', '18+')) NOT NULL,
    type VARCHAR(50) NOT NULL,
    language_original VARCHAR(50),
    country VARCHAR(50),
    budget BIGINT CHECK (budget >= 0) NOT NULL,
    box_office BIGINT CHECK (box_office >= 0) NOT NULL,
    preview VARCHAR(255) NOT NULL,
    total_views BIGINT DEFAULT 0 CHECK (total_views >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE content.filmwork_genres (
    filmwork_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (filmwork_id, genre_id),
    FOREIGN KEY (filmwork_id) REFERENCES content.filmwork (id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES content.genre (id) ON DELETE CASCADE
);

CREATE TABLE content.filmwork_actors (
    filmwork_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    PRIMARY KEY (filmwork_id, actor_id),
    FOREIGN KEY (filmwork_id) REFERENCES content.filmwork (id) ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES content.actor (id) ON DELETE CASCADE
);


CREATE INDEX idx_film_title ON content.filmwork(title);
CREATE INDEX idx_film_rating ON content.filmwork(rating);
CREATE INDEX idx_film_data_release ON content.filmwork(data_release);
CREATE INDEX idx_film_total_views ON content.filmwork(total_views);
CREATE INDEX idx_actor_full_name ON content.actor(full_name);
CREATE INDEX idx_genre_title ON content.genre(title);
CREATE INDEX idx_film_genre_film_id ON content.filmwork_genres(filmwork_id);
CREATE INDEX idx_film_genre_genre_id ON content.filmwork_genres(genre_id);
CREATE INDEX idx_film_actor_film_id ON content.filmwork_actors(filmwork_id);
CREATE INDEX idx_film_actor_actor_id ON content.filmwork_actors(actor_id);
