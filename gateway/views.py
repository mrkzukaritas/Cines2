"""Microservicio de pagos de CineMatch.

No contiene reglas de cine ni reservas: recibe una solicitud de Spring,
simula la autorización de pago y confirma el resultado al webhook de Spring.
"""

import json
import uuid
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST


METODOS_PERMITIDOS = {"TARJETA", "PSE", "EFECTIVO"}
pagos = {}


def respuesta_error(mensaje, status=400):
    return JsonResponse({"detalle": mensaje}, status=status)


@csrf_exempt
@require_POST
def procesar_pago(request):
    try:
        solicitud = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return respuesta_error("El cuerpo debe ser JSON válido.")

    reserva_id = solicitud.get("reservaId")
    metodo = str(solicitud.get("metodoPago", "")).upper()
    webhook_url = solicitud.get("webhookUrl")
    try:
        monto = float(solicitud.get("monto", 0))
    except (TypeError, ValueError):
        monto = 0

    if not reserva_id or not webhook_url:
        return respuesta_error("reservaId y webhookUrl son obligatorios.")
    if monto <= 0:
        return respuesta_error("El monto debe ser mayor que cero.")
    if metodo not in METODOS_PERMITIDOS:
        return respuesta_error("Método de pago no soportado. Usa TARJETA, PSE o EFECTIVO.")

    pago = {
        "transaccionId": str(uuid.uuid4()),
        "reservaId": reserva_id,
        "metodoPago": metodo,
        "monto": monto,
        "estado": "APROBADO",
        "fecha": datetime.now(timezone.utc).isoformat(),
    }
    pagos[pago["transaccionId"]] = pago

    try:
        callback = Request(
            webhook_url,
            data=json.dumps(pago).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(callback, timeout=10) as response:
            if response.status < 200 or response.status >= 300:
                raise URLError("Spring no confirmó el webhook.")
    except (HTTPError, URLError):
        pago["estado"] = "PENDIENTE_CONFIRMACION"
        return JsonResponse(
            {**pago, "detalle": "Pago creado, pero Spring aún no confirmó el webhook."},
            status=202,
        )

    return JsonResponse(pago, status=201)


@require_GET
def listar_pagos(_request):
    return JsonResponse(list(pagos.values()), safe=False)


@require_GET
def consultar_pago(_request, transaccion_id):
    pago = pagos.get(transaccion_id)
    if pago is None:
        return respuesta_error("Transacción no encontrada.", status=404)
    return JsonResponse(pago)
