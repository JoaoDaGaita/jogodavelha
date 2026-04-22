from game.board import Board
from game.minimax import MinimaxAI
from game.players import HumanPlayer, AIPlayer
from game.game import Game


def main():
    board = Board()
    ai_engine = MinimaxAI()

    p1 = HumanPlayer("X")
    p2 = AIPlayer("O", ai_engine)

    game = Game(board, p1, p2)
    game.play()


if __name__ == "__main__":
    main()