CREATE TABLE IF NOT EXISTS steamdata (
    id integer PRIMARY KEY AUTOINCREMENT,
    username text NOT NULL,
    password text NOT NULL
);