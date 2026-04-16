from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps import data_store as db
from datetime import date
from collections import defaultdict


@api_view(['GET'])
def reporte_diario(request):
    fecha = request.query_params.get('fecha', date.today().isoformat())
    ventas = db.get_ventas(fecha=fecha)

    total_ingresos = sum(v['total'] for v in ventas)
    total_transacciones = len(ventas)
    total_unidades = sum(v['cantidad'] for v in ventas)

    productos_vendidos = defaultdict(lambda: {'cantidad': 0, 'total': 0})
    for v in ventas:
        productos_vendidos[v['producto_nombre']]['cantidad'] += v['cantidad']
        productos_vendidos[v['producto_nombre']]['total'] += v['total']

    resumen_productos = [
        {'producto': nombre, **datos}
        for nombre, datos in productos_vendidos.items()
    ]

    return Response({
        'fecha': fecha,
        'total_ingresos': total_ingresos,
        'total_transacciones': total_transacciones,
        'total_unidades_vendidas': total_unidades,
        'detalle_ventas': ventas,
        'resumen_por_producto': resumen_productos,
    })


@api_view(['GET'])
def reporte_rango(request):
    fecha_inicio = request.query_params.get('fecha_inicio', date.today().isoformat())
    fecha_fin = request.query_params.get('fecha_fin', date.today().isoformat())

    todas_ventas = db.get_ventas()
    ventas_filtradas = [
        v for v in todas_ventas
        if fecha_inicio <= v['fecha'] <= fecha_fin
    ]

    por_dia = defaultdict(lambda: {'ingresos': 0, 'transacciones': 0})
    for v in ventas_filtradas:
        por_dia[v['fecha']]['ingresos'] += v['total']
        por_dia[v['fecha']]['transacciones'] += 1

    return Response({
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'total_ingresos': sum(v['total'] for v in ventas_filtradas),
        'total_transacciones': len(ventas_filtradas),
        'por_dia': [
            {'fecha': f, **datos}
            for f, datos in sorted(por_dia.items())
        ],
    })
