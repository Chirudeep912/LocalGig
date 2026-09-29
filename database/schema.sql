CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE gigs (
    id INTEGER PRIMARY KEY,
    client_id INTEGER,
    title VARCHAR(200),
    description TEXT,
    budget DECIMAL(10,2),
    status VARCHAR(30)
);

CREATE TABLE applications (
    id INTEGER PRIMARY KEY,
    gig_id INTEGER,
    worker_id INTEGER,
    proposal TEXT,
    status VARCHAR(30)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    gig_id INTEGER,
    worker_id INTEGER,
    status VARCHAR(30)
);

CREATE TABLE payments (
    id INTEGER PRIMARY KEY,
    client_id INTEGER,
    worker_id INTEGER,
    amount DECIMAL(10,2),
    status VARCHAR(30)
);