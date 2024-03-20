# Реализация тестового задания на должность Стажер бэкенд-разработчик
### Текст задания: https://pastebin.com/j2jtK3M8
### Исполнитель: Роман Сырбу
### Стек: FastAPI, SQLAlchemy + SQLite, Pytest

## Описание проекта
Три эндпоинта: 
1. /api/rating для выставления оценки комиксу
2. /api/comic/{comic_id}/rating/ для получения оценки комикса
3. / - главная страница. тут выводится сообщение о переходе к документации по адресу /api/docs

На данном скриншоте показана UI документация

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
В Dockerfile я включил сразу запуск тестов и последующий запуск. Результат тестов выводится в терминале при запуске контейнера, после чего запускается FastAPI приложение
1. Клонируем репозиторий
   ```
   git clone https://github.com/sssyrbu/test_task__backend_comic/
   ```
2. Перейдем в директорию проекта
   ```
   cd test_task__backend_comic/
   ```
3. Создаем docker image
   ```
   docker build -t comic_api .
   ```
4. Запускаем контейнер
   ```
   docker run -p 8081:8081 comic_api
   ```
   
Успешный запуск docker контейнера:

![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/669ad05e-dce5-4ef3-9e60-9258a1670a68)

## Тесты
Повторяем первые 6 шагов из [локального запуска](https://github.com/sssyrbu/test_task__backend_comic/blob/master/README.md#%D0%BB%D0%BE%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D0%BD%D0%B0-unix-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%D1%85).

7. Запускаем тесты
  ```
  pytest tests/
  ```

Успешный тест:

![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/8f4936a4-6c32-454f-9cb7-fb66917efccc)


### Адрес
http://0.0.0.0:8081/
### UI docs
http://0.0.0.0:8081/api/docs



![image](https://github.com/sssyrbu/test_task__backend_comic/assets/68150627/fd8db20a-aac0-4e93-aaae-65274a230d47)

