from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps import data_store as db


@api_view(['GET', 'POST'])
def ventas_list(request):
    if request.method == 'GET':
        fecha = request.query_params.get('fecha', None)
        ventas = db.get_ventas(fecha=fecha)
        return Response(ventas)

    if request.method == 'POST':
        data = request.data
        if not data.get('producto_id') or not data.get('cantidad'):
            return Response({'error': 'producto_id y cantidad son obligatorios'}, status=400)
        if int(data['cantidad']) <= 0:
            return Response({'error': 'La cantidad debe ser mayor a 0'}, status=400)

        nueva, error = db.add_venta({
            'producto_id': int(data['producto_id']),
            'cantidad': int(data['cantidad']),
        })
        if error:
            return Response({'error': error}, status=400)
        return Response(nueva, status=201)
