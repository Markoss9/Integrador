from src.aircraft import Jeep, Moto, Camion, Auto

class Player:
    def __init__(self, name: str, base_position: tuple):
        self.name = name
        self.base_position = base_position
        self.fleet = []
        self.score = 0

    def deploy_vehicles(self):
        """Crea y posiciona los vehículos del jugador."""
        vehicle_id = 1

        # 3 Jeeps
        for _ in range(3):
            self.fleet.append(Jeep(vehicle_id, self.base_position))
            vehicle_id += 1

        # 2 Motos
        for _ in range(2):
            self.fleet.append(Moto(vehicle_id, self.base_position))
            vehicle_id += 1

        # 2 Camiones
        for _ in range(2):
            self.fleet.append(Camion(vehicle_id, self.base_position))
            vehicle_id += 1

        # 3 Autos
        for _ in range(3):
            self.fleet.append(Auto(vehicle_id, self.base_position))
            vehicle_id += 1

    def update_score(self):
        """Actualiza el puntaje total basado en la carga entregada."""
        # Placeholder: en el futuro sumará puntos por recursos recolectados
        self.score = sum(r.value for v in self.fleet for r in v.cargo)

    def __repr__(self):
        return f"Player({self.name}, score={self.score}, fleet={len(self.fleet)})"
