DROP DATABASE users;

CREATE DATABASE users;

\connect users;

CREATE table IF NOT EXISTS users (
    id integer PRIMARY KEY,
    username varchar(80) UNIQUE NOT NULL,
    email varchar(120) UNIQUE NOT NULL
);

INSERT INTO users (id, username, email)
VALUES
  (1, 'alex', 'alex@k3s-dojo.com'),
  (2, 'bill', 'bill@k3s-dojo.com'),
  (3, 'connie', 'connie@k3s-dojo.com'),
  (4, 'derek', 'derek@k3s-dojo.com'),
  (5, 'ellen', 'ellen@k3s-dojo.com'),
  (6, 'francis', 'francis@k3s-dojo.com'),
  (7, 'gail', 'gail@k3s-dojo.com'),
  (8, 'helen', 'helen@k3s-dojo.com'),
  (9, 'igor', 'igor@k3s-dojo.com'),
  (10, 'julia', 'julia@k3s-dojo.com'),
  (11, 'kevin', 'kevin@k3s-dojo.com'),
  (12, 'liam', 'liam@k3s-dojo.com'),
  (13, 'mariam', 'mariam@k3s-dojo.com'),
  (14, 'neal', 'neal@k3s-dojo.com'),
  (15, 'olivia', 'olivia@k3s-dojo.com'),
  (16, 'paul', 'paul@k3s-dojo.com'),
  (17, 'quinn', 'quinn@k3s-dojo.com'),
  (18, 'riley', 'riley@k3s-dojo.com'),
  (19, 'sean', 'sean@k3s-dojo.com'),
  (20, 'tanya', 'tanya@k3s-dojo.com'),
  (21, 'umar', 'umar@k3s-dojo.com'),
  (22, 'vanya', 'vanya@k3s-dojo.com'),
  (23, 'william', 'william@k3s-dojo.com'),
  (24, 'xena', 'xena@k3s-dojo.com'),
  (25, 'yosef', 'yosef@k3s-dojo.com'),
  (26, 'zenia', 'zenia@k3s-dojo.com')
ON CONFLICT (id)
DO NOTHING;