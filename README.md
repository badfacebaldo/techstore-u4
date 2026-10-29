# TechStore U4 — Núcleo de negocio de pedidos

Práctica de Componentes de Lógica de Negocio · Unidad 4 (FIME · UANL). Dominio en Python con entidades DDD, Specification Pattern, máquina de estados, Domain Events y API REST con FastAPI. Todo en memoria: no requiere base de datos[cite: 33].

## Integrantes
- Osmel De Jesús Pérez Carrizales (2157401)[cite: 37]
- José Osvaldo Barcenas González (2158657)[cite: 37]
- Gerzayn Flores Rodriguez (2160879)[cite: 37]

## Estructura

```text
techstore-u4/
├── datos/             # CSV del paquete (clientes, productos, pedidos, detalle, escenarios)[cite: 33]
├── cargar_csv.py      # Cargador del paquete[cite: 33]
├── run_scenarios.py   # Ejecuta E01–E15 y genera la bitácora[cite: 33]
├── app/
│   ├── domain.py      # Money, Customer, OrderItem, Order, estados, eventos, excepciones[cite: 33]
│   ├── specifications.py # Specifications (AND / OR / NOT) y reglas de descuento[cite: 33]
│   └── api.py         # API REST (FastAPI)[cite: 33]
├── tests/             # Pruebas pytest (dominio, specifications, API)[cite: 33]
└── docs/              # Diagrama de estados, bitácora y reporte Word[cite: 33]
