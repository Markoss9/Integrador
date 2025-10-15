import random
import math

# ==========================================================
# Clase Mine
# ==========================================================
class Mine:
    def __init__(self, mine_type: str, position: tuple, radius: int, is_mobile: bool = False):
        self.type = mine_type
        self.position = position  # (x, y)
        self.radius = radius
        self.is_mobile = is_mobile

    def is_in_effect_area(self, x: float, y: float) -> bool:
        """Devuelve True si la posición (x, y) está dentro del radio de efecto de la mina."""
        distance = math.sqrt((self.position[0] - x) ** 2 + (self.position[1] - y) ** 2)
        return distance <= self.radius

    def __repr__(self):
        return f"Mine(type={self.type}, pos={self.position}, radius={self.radius}, mobile={self.is_mobile})"


# ==========================================================
# Clase Resource
# ==========================================================
class Resource:
    def __init__(self, resource_type: str, value: int, position: tuple):
        self.type = resource_type
        self.value = value
        self.position = position  # (x, y)

    def __repr__(self):
        return f"Resource(type={self.type}, value={self.value}, pos={self.position})"


# ==========================================================
# Clase Map
# ==========================================================
class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.resources = []  # lista de objetos Resource
        self.mines = []      # lista de objetos Mine

    def generate_random_map(self):
        """Distribuye aleatoriamente minas y recursos en el mapa."""
        self.resources = []
        self.mines = []

        # --- Recursos según el PDF ---
        resource_distribution = {
            "Persona": {"cantidad": 10, "valor": 50},
            "Ropa": {"cantidad": 10, "valor": 5},
            "Alimentos": {"cantidad": 10, "valor": 10},
            "Medicamentos": {"cantidad": 15, "valor": 20},
            "Armamentos": {"cantidad": 15, "valor": 50},
        }

        for tipo, data in resource_distribution.items():
            for _ in range(data["cantidad"]):
                x, y = random.randint(0, self.width), random.randint(0, self.height)
                self.resources.append(Resource(tipo, data["valor"], (x, y)))

        # --- Minas según el PDF ---
        mine_types = [
            ("O1", 10, False),  # Radio 10
            ("O2", 5, False),   # Radio 5
            ("T1", 10, False),
            ("T2", 5, False),
            ("G1", 7, True)     # Móvil
        ]

        for tipo, radio, movil in mine_types:
            # Se crean múltiples minas del mismo tipo (por ejemplo, 3 de cada)
            for _ in range(3):
                x, y = random.randint(0, self.width), random.randint(0, self.height)
                self.mines.append(Mine(tipo, (x, y), radio, movil))

    def display_map(self):
        """Muestra en consola los elementos del mapa (versión simple)."""
        print("\n--- MAPA GENERADO ---")
        print(f"Tamaño: {self.width} x {self.height}")
        print(f"Recursos totales: {len(self.resources)}")
        print(f"Minas totales: {len(self.mines)}\n")

        print("Recursos:")
        for r in self.resources[:10]:
            print(" ", r)
        if len(self.resources) > 10:
            print("  ...")

        print("\nMinas:")
        for m in self.mines[:10]:
            print(" ", m)
        if len(self.mines) > 10:
            print("  ...")