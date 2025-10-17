# Rescue Simulator

Simulador 2D de rescate competitivo donde dos jugadores controlan flotas de vehículos que recolectan recursos evitando minas y colisiones.

# FASE 1

Dejar lista la arquitectura base del proyecto para que en las siguientes fases puedan desarrollar la lógica del juego, los algoritmos y la simulación sin tener que reestructurar todo.

## Estructura del Proyecto

Deben crear una carpeta raíz llamada `rescue_simulator/` con esta estructura mínima:

rescue_simulator/
├── rescue_simulator.py # Archivo principal
├── src/
│ ├── game_engine.py # (motor del juego, se define después)
│ ├── aircraft.py # clases base de vehículos
│ ├── map_manager.py # gestión del mapa, minas y recursos
│ └── init.py
├── config/
│ ├── default_config.json # parámetros iniciales (dimensiones, cantidad de recursos)
│ └── init.py
├── data/
│ ├── simulations/ # guardado de simulaciones
│ └── statistics/ # resultados
├── tests/
│ ├── test_aircraft.py
│ ├── test_map_manager.py
│ └── init.py
└── README.md


**Consejo:**  
Usen un archivo `.gitignore` para evitar subir archivos temporales o de entorno (`__pycache__/`, `.env`, etc.).

---

## Clases Base y Diseño del Sistema

Definan las clases principales que luego se expandirán en las siguientes fases.  
Pueden hacerlo en pseudocódigo o Python básico con métodos vacíos (*placeholders*).

---

### Clase `Map` (en `map_manager.py`)

**Atributos:**
- `width`, `height`
- `resources` (lista de objetos `Resource`)
- `mines` (lista de objetos `Mine`)

**Métodos:**
- `generate_random_map()`: distribuye aleatoriamente recursos y minas.
- `display_map()`: (temporal) imprime una vista simple del mapa por consola.

---

### Clase `Mine`

**Atributos:**
- `type` (O1, O2, T1, T2, G1)
- `position` (x, y)
- `radius`
- `is_mobile` (bool)

**Métodos:**
- `is_in_effect_area(x, y)`: devuelve True si una posición está dentro del radio.

---

### Clase `Resource`

**Atributos:**
- `type` (persona, ropa, alimentos, medicamentos, armamentos)
- `value`
- `position` (x, y)

---

### Clase `Vehicle` (en `aircraft.py`)

**Atributos comunes:**
- `id`
- `type` (Jeep, Moto, Camión, Auto)
- `position`
- `capacity`
- `trips_remaining`
- `cargo`

**Métodos:**
- `move_to(x, y)`
- `collect(resource)`
- `return_to_base()`

Luego se podrán crear subclases (`Jeep`, `Moto`, etc.) que hereden de `Vehicle`.

---

### Clase `Player`

**Atributos:**
- `name`
- `base_position`
- `fleet` (lista de vehículos)
- `score`

**Métodos:**
- `deploy_vehicles()`
- `update_score()`

---

### Clase `GameEngine` (en `game_engine.py`, aún vacía)

Controlará el flujo principal del juego (inicialización, turnos, simulación).

---

## Archivo Principal `rescue_simulator.py`

Debe contener el punto de entrada del programa, algo como:

```python
from src.map_manager import Map
from src.aircraft import Vehicle

def main():
    print("=== Simulador de Rescate ===")

    # Inicialización del mapa
    game_map = Map(width=100, height=100)
    game_map.generate_random_map()

    # (Temporario) mostrar mapa
    game_map.display_map()

if __name__ == "__main__":
    main()


