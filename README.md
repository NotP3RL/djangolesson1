# Афиша

[Пример сайта](http://notp3rl.pythonanywhere.com/)

## Запуск

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python manage.py migrate
```

Запустите разработческий сервер

```
python manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `SECRET_KEY` — секретный ключ проекта
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Загрузка данных в бд

Для загрузки данных в базу данных можно использовать management команду:

```
python manage.py load_place {ссылка на json}
```

Json должен быть в [вот таком](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9B%D0%B0%D0%B3%D0%B5%D1%80%D1%8C%20%C2%AB%D0%9F%D0%BE%D0%B4%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D0%BD%D1%8B%D0%B9%C2%BB.json) формате

## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).