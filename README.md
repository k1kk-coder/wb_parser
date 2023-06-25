## _Парсер WB_

### _⏱ Описание_
Сервис реализует 4 конечные точки

- Добавить номенклатуру: пользователь указывает nm_id, сервис парсит данные с сайта
www.wildberries.ru и сохраняет их в базу данных PostgreSQL
- Получить товар по номенклатуре
- Получить все товары
- Удалить товар по номенклатуре
### _🚀 Инструкция по запуску на локальной машине в Docker 🐳_
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
docker-compose up -d
```
- По адресу localhost:8000/docs откройте документацию


### 🔧 _Стек технологий_

_Python, FastAPI, PostgreSQL, Docker, Celery_
