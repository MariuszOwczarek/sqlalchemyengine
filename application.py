from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy import text

sql_statements = """
CREATE DATABASE IF NOT EXISTS `blog`;

CREATE TABLE IF NOT EXISTS `blog`.`users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `blog`.`users` (username, email) VALUES ('john_doe', 'john@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('jane_smith', 'jane@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('alex_wong', 'alex@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('sarah_jones', 'sarah@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('michael_brown', 'michael@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('emily_rodriguez', 'emily@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('david_li', 'david@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('lisa_jackson', 'lisa@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('ryan_smith', 'ryan@example.com');
INSERT INTO `blog`.`users` (username, email) VALUES ('jessica_adams', 'jessica@example.com');
"""

def main():
    login = 'root'
    password = 'xxx'



    engine = create_engine(f"mysql+pymysql://{login}:{password}@localhost:3306")
    with engine.connect() as connection:
        for sql in sql_statements.split(";"):
            try:
                connection.execute(text(sql))
            except (IntegrityError, OperationalError):
                pass

        result = connection.execute(text("SELECT * FROM blog.users"))
        for row in result:
            print(row)


if __name__ == "__main__":
    main()