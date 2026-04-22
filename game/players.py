class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                pos = int(input(f"Jogador {self.symbol}, escolha (0-8): "))
                if pos in board.available_moves():
                    return pos
                print("Posição inválida!")
            except:
                print("Entrada inválida!")


class AIPlayer:
    def __init__(self, symbol, ai_engine):
        self.symbol = symbol
        self.ai = ai_engine

    def get_move(self, board):
        return self.ai.best_move(board)