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

## Запуск
### Локально (на UNIX системах)
1. Клонируем репозиторий
   ```
   git clone https://github.com/sssyrbu/test_task__backend_comic/
   ```
2. Перейдем в директорию проекта
   ```
   cd test_task__backend_comic/
   ```
3. Создадим виртуальное окружение
   ```
   python3 -m venv venv
   ```
4. Зайдем в виртуальное окружение
   ```
   source venv/bin/activate
   ```
5. Установим зависимости
   ```
   pip install -r requirements.txt
   ```
6. Перейдем в директорию с кодом
   ```
   cd app/
   ```
7. Запустим это приложение
   ```
   python3 main.py
   ```

### Docker
coming....

## Тесты
Повторяем первые 6 шагов из локального запуска.

7. Запускаем тесты
  ```
  pytest tests/
  ```

Успешный тест:

![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/8f4936a4-6c32-454f-9cb7-fb66917efccc)



