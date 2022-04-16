# Сайт "Куда пойти — Москва глазами Артёма"

Сайт состоит из общедоступной страницы с интерактивной картой на которой показаны интересные места Москвы для активного отдыха с подробными описаниями и комментариями.

Администраторы через админку могут добавлять на карту новые интересные места с описанием и фотографиями.

## Запуск

- Скачайте код с репозитория
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

    Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.


## Демо сайт

Пример работы сайта можно посмотреть здесь: https://orionapplepie.pythonanywhere.com/. Админка: https://orionapplepie.pythonanywhere.com/admin. Сайт доступен как с десктопов, так и на мобильных устройствах.
Демо данные взяты отсюда: https://github.com/devmanorg/where-to-go-frontend/.


## Добавление новых мест

Чтобы добавить новое место, войдите в админку сайта.
Перейдите в список "Интересные места города" и нажмите кнопку "Добавить интересное место города" (см. скрин ниже). Далее появиться форма добавления нового интересного места. Заполните следующие обязательные поля:
"Название", "Идентификатор места", "Короткое описание", "Полное описание", 
"Долгота", "Широта". Фотографии можно добавить позже.

![](/assets/img/images_list.png "Страница добавления интересных мест")


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).