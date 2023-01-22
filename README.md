# Docker

 Развертывание проекта Склады и запасы на базе образа Python:alpine.

## Документация по проекту:

На Linux машине перейти в папку с Dockerfile (корень проекта) и выплнить:

```bash
docker build -t py_stocks .
```

Затем запустить образ:

```bash
docker run -d -p 8000:8000 py_stocks
```

В браузере набрать:

```base
http://localhost:8000/api/v1/products/
```

или посылать запросы с помощью VSCode или Postman (примеры в корне Django-проекта).