# CineMatch - Microservicio de pagos (Django)

API encargada de gestionar y procesar los pagos de CineMatch, una aplicación web para la consulta y comparación de funciones y precios de cine.

Este microservicio está desarrollado en **Django** y funciona de manera independiente del backend principal. Spring Boot envía las solicitudes de pago mediante HTTP y Django confirma el resultado llamando al webhook de Spring Boot.

El microservicio se encarga exclusivamente de las operaciones relacionadas con los pagos. No gestiona las rutas de películas, cines, funciones ni reservas.

## Características

* Gestión y procesamiento de pagos mediante una API REST.
* Comunicación entre Django y Spring Boot mediante HTTP.
* Confirmación de resultados de pago mediante un webhook.
* Consulta del historial de transacciones.
* Consulta individual de transacciones por su identificador.
* Backend desarrollado en Python con Django.

## Tecnologías utilizadas

* **Python:** lenguaje de programación.
* **Django:** framework para el desarrollo del microservicio.
* **Spring Boot:** backend principal que recibe las confirmaciones de pago.
* **HTTP:** protocolo de comunicación entre los servicios.

## Endpoints de la API

La API dispone de los siguientes endpoints para gestionar y consultar las transacciones.

| Método HTTP | Endpoint                     | Descripción                                                                                                |
| ----------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `POST`      | `/api/pagos/procesar`        | Procesa y autoriza una transacción de pago, y llama al webhook de Spring Boot para confirmar el resultado. |
| `GET`       | `/api/pagos`                 | Obtiene la lista de transacciones registradas en Django.                                                   |
| `GET`       | `/api/pagos/{transaccionId}` | Consulta los detalles de una transacción específica mediante su identificador.                             |

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalados:

* Python compatible con las dependencias del proyecto.
* pip para instalar los paquetes de Python.
* Spring Boot ejecutándose en el puerto `8081` para recibir las confirmaciones de pago.

## Instalación

Clona el repositorio e ingresa al directorio del proyecto:

```bash
git clone https://github.com/mrkzukaritas/Cines2.git
cd Cines2
```

Instala las dependencias:

```bash
py -m pip install -r requirements.txt
```

## Ejecutar localmente

Inicia el servidor de desarrollo de Django en el puerto `8000`:

```bash
py manage.py runserver 8000
```

La API estará disponible localmente en:

`http://127.0.0.1:8000`

**Importante:** Spring Boot debe estar activo en el puerto `8081` para recibir las confirmaciones enviadas mediante el webhook.

## Integración con Spring Boot

La comunicación entre los dos servicios sigue este flujo general:

1. Spring Boot envía una solicitud HTTP a Django para procesar un pago.
2. Django procesa la transacción y determina el resultado.
3. Django llama al webhook de Spring Boot para notificar el resultado del pago.
4. Spring Boot recibe la confirmación y continúa con el flujo correspondiente de la aplicación.

## Consultar transacciones

Para consultar las transacciones registradas localmente, utiliza:

```http
GET /api/pagos
```

Para consultar una transacción específica:

```http
GET /api/pagos/{transaccionId}
```

## Alcance del microservicio

Este microservicio es responsable exclusivamente de la gestión de pagos y la comunicación de sus resultados con Spring Boot.

No es responsable de gestionar películas, cines, funciones ni reservas, ya que estas funcionalidades corresponden a otros componentes del sistema CineMatch.

## Licencia

Consulta el archivo `LICENSE` del repositorio para conocer las condiciones de uso y distribución del proyecto.
