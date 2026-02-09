# ORM Migrations

Django-проект для управления учениками и учителями.

> Проект разработан в рамках учебного процесса [Нетологии](https://netology.ru/).

## Требования

- Python 3.10+
- PostgreSQL 12+
- Django 6.0.2
- psycopg2-binary 2.9.11

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository_url>
cd orm_migrations
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка базы данных

1. Создайте базу данных PostgreSQL:

```bash
createdb -U postgres netology_orm_migrations
```

2. Настройте подключение в `website/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_orm_migrations',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'ваш_пользователь',
        'PASSWORD': 'ваш_пароль',
    }
}
```

## Запуск

1. Примените миграции:
```bash
python manage.py migrate
```

2. Загрузите начальные данные из JSON:
```bash
python manage.py loaddata school.json
```

3. Запустите сервер:
```bash
python manage.py runserver
```

4. Откройте браузер по адресу http://127.0.0.1:8000/school/


## Модели

### Teacher (Учитель)
- `name` - ФИО учителя
- `subject` - предмет

### Student (Ученик)
- `name` - ФИО ученика
- `group` - класс/группа
- `teachers` - связь ManyToMany с учителями
