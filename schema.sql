DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS ingredient;
CREATE TABLE user (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
);


CREATE TABLE ingredient (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ingredient_name TEXT NOT NULL,
  user_id INT NOT NULL,
  yaminabe_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id)
);

