# TechStore U4 — Núcleo de negocio de pedidos

Práctica de Componentes de Lógica de Negocio · Unidad 4 (FIME · UANL). Dominio en Python con entidades DDD, Specification Pattern, máquina de estados, Domain Events y API REST con FastAPI. Todo en memoria: no requiere base de datos.

## Integrantes
- Osmel De Jesús Pérez Carrizales (2157401)
- José Osvaldo Barcenas González (2158657)
- Gerzayn Flores Rodriguez (2160879)

## Estructura

```text
techstore-u4/
├── datos/             # CSV del paquete (clientes, productos, pedidos, detalle, escenarios)
├── cargar_csv.py      # Cargador del paquete
├── run_scenarios.py   # Ejecuta E01–E15 y genera la bitácora
├── app/
│   ├── domain.py      # Money, Customer, OrderItem, Order, estados, eventos, excepciones
│   ├── specifications.py # Specifications (AND / OR / NOT) y reglas de descuento
│   └── api.py         # API REST (FastAPI)
├── tests/             # Pruebas pytest (dominio, specifications, API)
└── docs/              # Diagrama de estados, bitácora y reporte Word
