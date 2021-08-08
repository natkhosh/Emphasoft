# Emphasoft
Simple CRUD application

Тестирование API можно сделать например с помощью [curl](https://curl.haxx.se/) или [httpie](https://github.com/jakubroztocil/httpie#installation), или можно использовать [Postman](https://www.postman.com/)

Регистрация пользователя

POST/api/v1/registration/ Регистрация, передать login и password
```
http POST http://127.0.0.1:8000/api/v1/registration/ username='user' password='user!'
```
Тебования:

login:
Максимум 150 символов.
Буквы, цифры и только @/./+/ -/_.
password:
Не должен совпадать с вашим именем или другой персональной информацией или быть слишком похожим на неё.
Должен содержать как минимум 8 символов.
Не может быть одним из широко распространённых паролей.
Не может состоять только из цифр
Получить токен

POST/api/api-token-auth/ Получить токен, передать login и password


