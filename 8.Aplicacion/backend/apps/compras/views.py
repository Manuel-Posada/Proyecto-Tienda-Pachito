from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps import data_store as db


@api_view(['GET', 'POST'])
def compras_list(request):
    if request.method == 'GET':
        return Response(db.get_compras())

    if request.method == 'POST':
        data = request.data
        if not data.get('producto_id') or not data.get('cantidad'):
            return Response({'error': 'producto_id y cantidad son obligatorios'}, status=400)

        nueva, error = db.add_compra({
            'producto_id': int(data['producto_id']),
            'cantidad': int(data['cantidad']),
            'costo_unitario': int(data.get('costo_unitario', 0)),
        })
        if error:
            return Response({'error': error}, status=400)
        return Response(nueva, status=201)
