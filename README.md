## Парсер WB

### ⏱ Описание
Сервис реализует 4 конечные точки

- Добавить номенклатуру: пользователь указывает nm_id, сервис парсит данные с сайта
www.wildberries.ru и сохраняет их в базу данных PostgreSQL
- Получить товар по номенклатуре
- Получить все товары
- Удалить товар по номенклатуре
### 🚀 Инструкция по запуску на локальной машине в Docker 🐳
- Клонируйте проект
```
git clone <ссылка>
``` 
- Перейдите в папку infra и создайте .env файл по шаблону:
```
DB_NAME=postgres
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
REDIS_HOST=redis
```
- Находясь в папке infra выполните команду:
```
docker-compose up
```
- Перейдите в контейнер backend
```
docker exec -it CONTAINER_ID bash
```
- Находясь в контейнере выполните команды:
```
cd ..
alembic upgrade head
```
- По адресу localhost:8000/docs откройте документацию


### 🔧 Стек технологий

_Python, FastAPI, PostgreSQL, Docker, Celery_
