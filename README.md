## Установка:

Клонируем проект:  

    git clone https://github.com/anza-afk/book_api_test_task.git

Создаём .env файл в корне с переменными (как в файле с примером .env_example):

##### Настройки для базы данных MYSQL (Можно ставить такими же, как и в примере):

    DB_NAME=library_db
    DB_USER=library_admin
    DB_PASSWORD=97ugAz!24i4F
    DB_HOST=db
    DB_PORT=3306

##### Настройки для Redis (Можно ставить такими же, как и в примере):

    REDIS_HOST=redis
    REDIS_PORT=6379

##### Настройка почтового ящика для отправки письма при регистрации пользователя:

    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.___.__'  # Адрес SMTP сервера вашего email
    EMAIL_PORT=465
    EMAIL_HOST_USER='___@___.__'  # Ваш email
    EMAIL_HOST_PASSWORD='______'  # Пароль от вашего email

## Запуск через docker-compose:

    docker-compose up --build -d


## Эндпоинты API:

    /api/books/ - Получение списка всех книг. и создание новой книги
    /api/books/<id> - Обновления информации о книге, получения информации о конкретной книге удаление книги
    /api/register/ - Принимает POST запрос на регистрацию нового пользователя м полями username, email и password
