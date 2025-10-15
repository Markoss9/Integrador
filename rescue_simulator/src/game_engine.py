from src.map_manager import Map
from src.aircraft import Vehicle
from src.player import Player  # si lo separas en otro archivo (opcional)

class GameEngine:
    def __init__(self, width=100, height=100):
        self.map = Map(width, height)
        self.players = []

    def add_player(self, player):
        """Agrega un jugador al motor del juego."""
        self.players.append(player)

    def initialize_game(self):
        """Inicializa el mapa y los jugadores."""
        self.map.generate_random_map()
        for player in self.players:
            player.deploy_vehicles()

    def start_simulation(self):
        """Inicia la simulación (placeholder)."""
        print("Simulación iniciada... (fase futura)")

    def __repr__(self):
        return f"GameEngine(players={len(self.players)}, map={self.map.width}x{self.map.height})"
