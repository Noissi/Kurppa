CREATE TABLE accounts (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR (20) UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE roles (
    role_id serial PRIMARY KEY,
    role_name VARCHAR (255) UNIQUE NOT NULL
);

CREATE TABLE account_roles (
    user_id INT NOT NULL,
	role_id INT NOT NULL,
	grant_date TIMESTAMP,
	PRIMARY KEY (user_id, role_id),
	FOREIGN KEY (role_id)
		REFERENCES roles (role_id),
	FOREIGN KEY (user_id)
		REFERENCES accounts (user_id)
);

CREATE TABLE birds (
    bird_id CHAR (6) PRIMARY KEY,
    name_lat VARCHAR (255) UNIQUE NOT NULL,
    rarity VARCHAR (1),
    name_fi VARCHAR (255) UNIQUE NOT NULL,
    name_swe VARCHAR (255) UNIQUE NOT NULL,
    name_eng VARCHAR (255) UNIQUE NOT NULL,
    orderr VARCHAR (255) NOT NULL,
    family VARCHAR (255) NOT NULL,
    image VARCHAR (255)
);

CREATE TABLE sights (
    sight_id serial PRIMARY KEY,
    name_fi VARCHAR (255) NOT NULL,
    amount INT NOT NULL,
    place VARCHAR (255),
    date TIMESTAMP,
    username VARCHAR (20) NOT NULL
);
