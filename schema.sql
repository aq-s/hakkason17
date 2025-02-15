DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS yaminabe;

CREATE TABLE yaminabe (
  yaminabe_id INT AUTO_INCREMENT PRIMARY KEY,
  yaminabe_name TEXT PRIMARY KEY NOT NULL,
  yaminabe_kansei INTEGER NOT NULL,
);

CREATE TABLE ingredient (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ingredient_name TEXT NOT NULL,
  yaminabe_id INTEGER NOT NULL,
  FOREIGN KEY (yaminabe_id) REFERENCES yaminabe(yaminabe_id)
);

