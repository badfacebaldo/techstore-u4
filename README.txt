========================================================================
TechStore U4 - Núcleo de negocio de pedidos (FIME - UANL)
========================================================================

INTEGRANTES
- Osmel De Jesús Pérez Carrizales (2157401)
- José Osvaldo Barcenas González (2158657)
- Gerzayn Flores Rodriguez (2160879)

ESTRUCTURA DEL PROYECTO
- datos/: CSV del paquete (clientes, productos, pedidos, detalle, escenarios)
- cargar_csv.py: Cargador del paquete
- run_scenarios.py: Ejecuta E01-E15 y genera la bitácora
- app/:
    - domain.py: Money, Customer, OrderItem, Order, estados, eventos, excepciones
    - specifications.py: Specifications (AND / OR / NOT) y reglas de descuento
    - api.py: API REST (FastAPI)
- tests/: Pruebas pytest (dominio, specifications, API)
- docs/: Diagrama de estados, bitácora y reporte Word

INSTALACIÓN
Requiere Python 3.11 o superior.

    python -m venv .venv
    # Windows PowerShell: .venv\Scripts\Activate.ps1
    # Windows CMD:        .venv\Scripts\activate.bat
    # macOS / Linux:      source .venv/bin/activate
    python -m pip install -r requirements.txt

COMANDOS DE EJECUCIÓN
- Cargar los 16 pedidos:       python cargar_csv.py
- Ejecutar los 15 escenarios:   python run_scenarios.py
- Ejecutar pruebas:             python -m pytest -q
- Iniciar API REST:             uvicorn app.api:app --reload

ACCESO A LA API (Con servidor en ejecución)
- Swagger UI:      http://127.0.0.1:8000/docs
- Contrato OpenAPI: http://127.0.0.1:8000/openapi.json

REGLAS DE NEGOCIO
- Money no admite importes negativos; usar Decimal, no float.
- Máximo 20 unidades por pedido (suma de cantidades).
- Descuento 10%: cliente VIP, total >500 MXN, >=4 unidades, sin promoción.
- Descuento 5%: total >5000 MXN, sin promoción. Prioridad 10% si ambas se cumplen.
- Transiciones: DRAFT -> CONFIRMED -> SHIPPED -> DELIVERED / RETURNED / CANCELLED.
========================================================================