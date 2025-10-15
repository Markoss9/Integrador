from src.map_manager import Map
from src.player import Player
from src.game_engine import GameEngine

def main():
    print("=== SIMULADOR DE RESCATE ===")

    # Crear motor del juego
    engine = GameEngine(width=100, height=100)

    # Crear jugadores
    player1 = Player("Jugador 1", base_position=(0, 0))
    player2 = Player("Jugador 2", base_position=(100, 100))

    # Agregarlos al motor
    engine.add_player(player1)
    engine.add_player(player2)

    # Inicializar juego
    engine.initialize_game()

    # Mostrar mapa generado
    engine.map.display_map()

    # Mostrar flotas
    print("\nFlota de Jugador 1:")
    for v in player1.fleet:
        print(" ", v)

    print("\nFlota de Jugador 2:")
    for v in player2.fleet:
        print(" ", v)

if __name__ == "__main__":
    main()
