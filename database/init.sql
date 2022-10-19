CREATE SCHEMA service;

CREATE TABLE IF NOT EXISTS service.users(
    id SERIAL NOT NULL, full_name VARCHAR NOT NULL,
    login VARCHAR NOT NULL, password VARCHAR NOT NULL
);

INSERT INTO service.users(full_name, login, password) VALUES(
    'Test Account', 'test', 'test'
);

-- Домашняя работа, задание №1

INSERT INTO
    service.users(full_name, login, password)
VALUES
    ('Степанов Фёдор', 'stepanov_fedr', 'vlwgZQDawkGL6Zh7'),
    ('Горячев Станислав', 'goryachev_stanislav', 'tZI0EsYz2UolqK6H'),
    ('Толкачев Василий', 'tolkachev_vasiliy', 'fr5frB6JRLZ3Qwq2'),
    ('Ермолов Глеб', 'ermolov_gleb', 'xL0LwGlziPyWIxio'),
    ('Алексеев Алексей', 'alekseev_aleksiy', 'MqXfaOJjKMpLLjaz'),
    ('Дмитриев Елисей', 'dmitriev_elisey', 'a7vDGN4G6eDx1o8N'),
    ('Иванов Иван', 'ivanov_ivan', 'a7vDGN4G6eDx1o8N'),
    ('Чернов Александр', 'chernov_aleksandr', 'HjDyXAZ3tvszW8sI'),
    ('Михайлов Егор', 'mixaylov_egor', 'HjDyXAZ3tvszW8sI')
;
