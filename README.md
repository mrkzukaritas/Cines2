# CineMatch API (Django)

Esta aplicación es la API Gateway del proyecto. Recibe las solicitudes del frontend y las reenvía por HTTP al backend de negocio hecho en Spring Boot.

## Ejecutar localmente

1. Inicia `cinematch-backend` en el puerto `8081`.
2. Instala las dependencias: `py -m pip install -r requirements.txt`.
3. Ejecuta la API: `py manage.py runserver 8000`.

El frontend debe usar `http://127.0.0.1:8000/api` como URL base. Puedes verificar la comunicación en `GET /api/peliculas`.

Para usar otra dirección del backend, define la variable `SPRING_BACKEND_URL` antes de iniciar Django.
