# Library


## Стек

python 3.8
Django 3.2
Django REST Framework 3.12
Djoser 2.1

## Дисклеймер

Для удобства запуска в репозитории присутствует файл .env. В реальном репозитории так поступать не стоит

## Инструкции по запуску

Linux:

python3 -m venv venv

. venv/bin/activate

Windows:

python -m venv venv

source venv/Scripts/activate

Далее:

pip install -r requirements.txt

cd event

python manage.py runserver

## Доступ в админ панель

email: admin@admin.com

password: admin

## Запросы

### Получение токена

http://localhost:8000/auth/jwt/create

Запрос:

{

    "email": "admin@admin.com",
    
    "password": "admin"
    
}

Ответ:

{

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTU0NTgwMCwianRpIjoiMjViOWU3ZDkyYmI0NDEzOGI5MjMzMzdiMmJhNDI5OTkiLCJ1c2VyX2lkIjoxfQ.1JM4rDA1tzSUBR7UTS1aRyvKOArQAr86nkfDsk5qYIg",
    
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NTQ1ODAwLCJqdGkiOiJjMzY5MWE1YzQxNzA0NTc4OGZhZWRkZmZiYWFmMzBiZSIsInVzZXJfaWQiOjF9.F1yU8XC-T60i3I_i4ml7u8LVsP0jWno3Ktgy8oYfK7k"
    
}

### Создание организации:

http://127.0.0.1:8000/organizations/

POST

Headers
 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NTQ1ODAwLCJqdGkiOiJjMzY5MWE1YzQxNzA0NTc4OGZhZWRkZmZiYWFmMzBiZSIsInVzZXJfaWQiOjF9.F1yU8XC-T60i3I_i4ml7u8LVsP0jWno3Ktgy8oYfK7k

Body:

{

    "title": "Yandex", 
    
    "description": "IT", 
    
    "address": "Москва, ул. Льва Толстого, 16", 
    
    "postcode": "119021"
    
}

Ответ:

{
    "id": 1,
    
    "title": "Yandex",
    
    "description": "IT",
    
    "address": "Москва, ул. Льва Толстого, 16",
    
    "postcode": "119021"
    
}

### Создание мероприятия

http://127.0.0.1:8000/organizations/

POST

Headers
 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NTQ1ODAwLCJqdGkiOiJjMzY5MWE1YzQxNzA0NTc4OGZhZWRkZmZiYWFmMzBiZSIsInVzZXJfaWQiOjF9.F1yU8XC-T60i3I_i4ml7u8LVsP0jWno3Ktgy8oYfK7k

Body:

Postman -> Body -> form-data

title: Лидеры цифровой трансформации
description: Хакатон
organizations: 1 (id организации)
organizations: 2 (id другой организации при необходимости)
image -> File: выбрать файл
date: 2023-05-17

Ответ:

{

    "title": "Лидеры цифровой трансформации",
    
    "description": "Хакатон",
    
    "organizations": [
    
        {
        
            "id": 1,
            
            "title": "Yandex",
            
            "description": "IT",
            
            "address": "Москва, ул. Льва Толстого, 16",
            
            "postcode": "119021"
            
        },
        
    ],
    
    "image": "http://localhost:8000/media/images/LCT_NEuhTeN.jpg",
    
    "date": "2023-05-17"
    
}

### Просмотр мероприятия

http://127.0.0.1:8000/organizations/{id}

GET

Headers
 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NTQ1ODAwLCJqdGkiOiJjMzY5MWE1YzQxNzA0NTc4OGZhZWRkZmZiYWFmMzBiZSIsInVzZXJfaWQiOjF9.F1yU8XC-T60i3I_i4ml7u8LVsP0jWno3Ktgy8oYfK7k

Ответ:

{

    "id": 1,
    
    "organizations": [
    
        {
        
            "title": "Yandex",
            
            "description": "IT",
            
            "address": "119021 Москва, ул. Льва Толстого, 16",
            
            "users": [
            
                "admin"
                
            ]
            
        }
        
    ],
    
    "title": "Лидеры цифровой трансформации",
    
    "description": "Хакатон",
    
    "image": "http://localhost:8000/media/images/LCT.jpg",
    
    "date": "2023-05-17"
    
}

### Просмотр всех мероприятий

GET 

Headers
 
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1NTQ1ODAwLCJqdGkiOiJjMzY5MWE1YzQxNzA0NTc4OGZhZWRkZmZiYWFmMzBiZSIsInVzZXJfaWQiOjF9.F1yU8XC-T60i3I_i4ml7u8LVsP0jWno3Ktgy8oYfK7k

http://127.0.0.1:8000/organizations/

Поддерживается фильтрация по датам

http://localhost:8000/events/?date_after=2023-06-01&date_before=2023-12-31

пагинация

http://localhost:8000/events/?limit=2&page=2

поиск по названию

http://localhost:8000/events/??search=something

Ответ:

{

    "count": 1,
    
    "next": null,
    
    "previous": null,
    
    "results": [
    
        {
        
            "id": 4,
            
            "organizations": [
            
                {
                
                    "title": "Yandex",
                    
                    "description": "IT",
                    
                    "address": "119021 Москва, ул. Льва Толстого, 16",
                    
                    "users": [
                    
                        "admin"
                        
                    ]
                    
                },
                
                {
                
                    "title": "СПБ ГБУ Централизованная библиотечная система Выборгского района",
                    
                    "description": "12 уникальных библиотек Выборгского района Петербурга",
                    
                    "address": "194156 г. Санкт-Петербург\r\nпр. Энгельса, д. 13/2",
                    
                    "users": [
                    
                        "Konstantin"
                        
                    ]
                    
                }
                
            ],
            
            "title": "Выставка \"Современные технологии оцифровки библиотечного фонда\"",
            
            "description": "Выставка",
            
            "image": "http://localhost:8000/media/images/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2023-05-30_192429633.png",
            
            "date": "2023-06-21"
            
        }
        
    ]
    
}
