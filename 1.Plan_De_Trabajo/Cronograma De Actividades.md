gantt
    title 📊 Cronograma Tienda Pachito (Scrum)
    dateFormat  YYYY-MM-DD
    todayMarker on

    section Sprint 1 – Core (Inicio desarrollo)
    HU-01 Registro de productos           :a1, 2026-04-16, 5d
    └─ Registrar producto                :a2, after a1, 2d
    └─ Editar precio                     :a3, after a2, 1d

    HU-02 Registro de ventas             :b1, 2026-04-18, 5d
    └─ Registrar venta                   :b2, after b1, 1d
    └─ Ingresar cantidad                 :b3, after b2, 1d
    └─ Calcular total                    :b4, after b3, 1d

    HU-03 Control de inventario          :c1, 2026-04-20, 4d
    └─ Descontar stock                   :c2, after c1, 1d
    └─ Validar stock                     :c3, after c2, 1d
    └─ Mostrar stock                     :c4, after c3, 1d

    section Sprint 2 – Funcionalidades clave
    HU-04 Registro de compras            :d1, 2026-04-25, 5d
    └─ Registrar compra                  :d2, after d1, 1d
    └─ Actualizar stock                  :d3, after d2, 1d
    └─ Guardar fecha                     :d4, after d3, 1d

    HU-05 Reporte diario                 :e1, 2026-04-27, 5d
    └─ Ver ventas del día                :e2, after e1, 1d
    └─ Total vendido                     :e3, after e2, 1d
    └─ Filtrar por fecha                 :e4, after e3, 1d

    section Sprint 3 – Cierre y mejoras
    HU-06 Alertas de stock bajo          :f1, 2026-05-03, 4d
    └─ Definir stock mínimo              :f2, after f1, 1d
    └─ Mostrar alerta                    :f3, after f2, 1d

    section Entregas
    Sprint 1 Finalizado                  :milestone, 2026-04-24, 0d
    Sprint 2 Finalizado                  :milestone, 2026-05-02, 0d
    Entrega Final Proyecto               :milestone, 2026-05-09, 0d
