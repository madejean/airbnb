CREATE USER 'airbnb_user_dev'@'%' IDENTIFIED BY 'password';
CREATE USER 'airbnb_user_prod'@'%' IDENTIFIED BY 'password';

CREATE DATABASE airbnb_dev
       CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE DATABASE airbnb_prod
       CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON airbnb_dev . * TO 'airbnb_user_dev'@'%';
GRANT ALL PRIVILEGES ON airbnb_prod . * TO 'airbnb_user_prod'@'%';
