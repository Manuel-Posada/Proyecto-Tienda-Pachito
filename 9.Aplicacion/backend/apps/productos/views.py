from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps import data_store as db


@api_view(['GET', 'POST'])
def productos_list(request):
    if request.method == 'GET':
        productos = db.get_productos()
        alertas = db.get_alertas_stock()
        alertas_ids = {p['id'] for p in alertas}
        for p in productos:
            p['alerta_stock'] = p['id'] in alertas_ids
        return Response(productos)

    if request.method == 'POST':
        data = request.data
        if not data.get('nombre') or data.get('precio') is None:
            return Response({'error': 'nombre y precio son obligatorios'}, status=400)
        nuevo = db.add_producto(data)
        return Response(nuevo, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, pk):
    producto = db.get_producto(pk)
    if not producto:
        return Response({'error': 'Producto no encontrado'}, status=404)

    if request.method == 'GET':
        return Response(producto)

    if request.method == 'PUT':
        actualizado = db.update_producto(pk, request.data)
        return Response(actualizado)

    if request.method == 'DELETE':
        db.delete_producto(pk)
        return Response(status=204)


@api_view(['GET'])
def alertas_stock(request):
    alertas = db.get_alertas_stock()
    return Response(alertas)
