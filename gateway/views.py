"""Puerta de entrada HTTP entre el frontend y el backend Spring Boot."""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


SPRING_BACKEND_URL = os.getenv("SPRING_BACKEND_URL", "http://127.0.0.1:8081")


@csrf_exempt
def proxy(request, resource=""):
    """Reenvía el método, cuerpo y respuesta al microservicio de negocio."""
    path = f"/api/{resource}".rstrip("/") or "/api"
    query = request.META.get("QUERY_STRING")
    destination = f"{SPRING_BACKEND_URL}{path}"
    if query:
        destination = f"{destination}?{query}"

    headers = {"Accept": request.headers.get("Accept", "application/json")}
    if request.content_type:
        headers["Content-Type"] = request.content_type
    body = request.body if request.method not in {"GET", "DELETE"} else None

    try:
        spring_request = Request(destination, data=body, headers=headers, method=request.method)
        with urlopen(spring_request, timeout=10) as response:
            return HttpResponse(
                response.read(),
                status=response.status,
                content_type=response.headers.get_content_type(),
            )
    except HTTPError as error:
        return HttpResponse(
            error.read(),
            status=error.code,
            content_type=error.headers.get_content_type(),
        )
    except URLError:
        return JsonResponse(
            {
                "error": "El backend Spring Boot no está disponible.",
                "detalle": "Inicia el proyecto cinematch-backend en el puerto 8081.",
            },
            status=503,
        )

# Create your views here.
