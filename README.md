# Rescue Simulator

Simulador 2D de rescate competitivo donde dos jugadores controlan flotas de vehículos que recolectan recursos evitando minas y colisiones.

# FASE 1

## Estructura del Proyecto

rescue_simulator/
├── rescue_simulator.py            # Archivo principal
├── src/
│   ├── game_engine.py             # (motor del juego, se define después)
│   ├── aircraft.py                # clases base de vehículos
│   ├── map_manager.py             # gestión del mapa, minas y recursos
│   └── __init__.py
├── config/
│   ├── default_config.json        # parámetros iniciales (dimensiones, cantidad de recursos)
│   └── __init__.py
├── data/
│   ├── simulations/               # guardado de simulaciones
│   └── statistics/                # resultados
├── tests/
│   ├── test_aircraft.py
│   ├── test_map_manager.py
│   └── __init__.py
└── README.md


## Clases Base y Diseño del Sistema

Clase Map (en map_manager.py)

Atributos:

width, height

resources (lista de objetos Resource)

mines (lista de objetos Mine)

Métodos:

generate_random_map(): distribuye aleatoriamente recursos y minas.

display_map(): (temporal) imprime una vista simple del mapa por consola.

🔹 Clase Mine

Atributos:

type (O1, O2, T1, T2, G1)

position (x, y)

radius

is_mobile (bool)

Métodos:

is_in_effect_area(x, y): devuelve True si una posición está dentro del radio.

🔹 Clase Resource

Atributos:

type (persona, ropa, alimentos, medicamentos, armamentos)

value

position (x, y)

🔹 Clase Vehicle (en aircraft.py)

Atributos comunes:

id

type (Jeep, Moto, Camión, Auto)

position

capacity

trips_remaining

cargo

Métodos:

move_to(x, y)

collect(resource)

return_to_base()

Luego se podrán crear subclases (Jeep, Moto, etc.) que hereden de Vehicle.

🔹 Clase Player

Atributos:

name

base_position

fleet (lista de vehículos)

score

Métodos:

deploy_vehicles()

update_score()

🔹 Clase GameEngine (en game_engine.py, aún vacía)

Controlará el flujo principal del juego (inicialización, turnos, simulación).