DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS yaminabe;

CREATE TABLE yaminabe (
  yaminabe_id INTEGER PRIMARY KEY AUTOINCREMENT,
  yaminabe_name TEXT NOT NULL
  --yaminabe_kansei INTEGER NOT NULL
);

CREATE TABLE ingredient (
  id INTEGER  PRIMARY KEY AUTOINCREMENT,
  ingredient_name TEXT NOT NULL,
  yaminabe_id INTEGER NOT NULL,
  FOREIGN KEY (yaminabe_id) REFERENCES yaminabe(yaminabe_id)
);

