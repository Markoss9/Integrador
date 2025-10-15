# ==========================================================
# Clase Vehicle
# ==========================================================
class Vehicle:
    def __init__(self, vehicle_id: int, vehicle_type: str, position: tuple, capacity: int, trips_remaining: int):
        self.id = vehicle_id
        self.type = vehicle_type
        self.position = position
        self.capacity = capacity
        self.trips_remaining = trips_remaining
        self.cargo = []

    # ------------------------------------------------------
    def move_to(self, x: float, y: float):
        """Mueve el vehículo a una nueva posición (placeholder)."""
        self.position = (x, y)

    # ------------------------------------------------------
    def collect(self, resource):
        """Intenta recoger un recurso (placeholder)."""
        if len(self.cargo) < self.capacity:
            self.cargo.append(resource)
        else:
            print(f"Vehículo {self.id} está lleno.")

    # ------------------------------------------------------
    def return_to_base(self):
        """Simula el retorno del vehículo a la base (placeholder)."""
        self.trips_remaining -= 1
        self.cargo = []

    # ------------------------------------------------------
    def __repr__(self):
        return f"Vehicle(id={self.id}, type={self.type}, pos={self.position}, cargo={len(self.cargo)})"


# ==========================================================
# Subclases de vehículos (pueden tener reglas distintas)
# ==========================================================
class Jeep(Vehicle):
    def __init__(self, vehicle_id, position):
        super().__init__(vehicle_id, "Jeep", position, capacity=5, trips_remaining=2)


class Moto(Vehicle):
    def __init__(self, vehicle_id, position):
        super().__init__(vehicle_id, "Moto", position, capacity=1, trips_remaining=1)


class Camion(Vehicle):
    def __init__(self, vehicle_id, position):
        super().__init__(vehicle_id, "Camion", position, capacity=10, trips_remaining=3)


class Auto(Vehicle):
    def __init__(self, vehicle_id, position):
        super().__init__(vehicle_id, "Auto", position, capacity=3, trips_remaining=1)
