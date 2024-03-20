# Реализация тестового задания на должность Стажер бэкенд-разработчик
### Текст задания: https://pastebin.com/j2jtK3M8
### Исполнитель: Роман Сырбу
### Стек: FastAPI, SQLAlchemy + SQLite, Pytest

## Описание проекта
Три эндпоинта: 
1. /api/rating для выставления оценки комиксу
2. /api/comic/{comic_id}/rating/ для получения оценки комикса
3. / - главная страница. тут выводится сообщение о переходе к документации по адресу /api/docs

На данном скриншоте показана UI документация по адресу http://0.0.0.0:8081/api/docs

![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/835e399e-1728-404d-ade6-a6473114940d)

Два объекта в ORM: Comic и Rating. Объекты лежат в /app/models/db_models.py в исходном коде.

### Структура проекта:

![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/37ff6776-21e2-458d-9eea-b507075e597a)


