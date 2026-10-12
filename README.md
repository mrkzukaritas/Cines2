# CineMatch - Microservicio de pagos (Django)

Esta aplicación procesa pagos de forma independiente. Spring Boot le envía una solicitud de pago por HTTP y Django confirma el resultado llamando al webhook de Spring. No reenvía las rutas de películas, cines, funciones o reservas.

## Ejecutar localmente

1. Instala las dependencias: `py -m pip install -r requirements.txt`.
2. Ejecuta la API: `py manage.py runserver 8000`.

Spring Boot debe estar activo en el puerto `8081` para confirmar los pagos. Puedes consultar las transacciones locales en `GET /api/pagos`.
