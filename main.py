from game.board import Board
from game.minimax import MinimaxAI
from game.players import HumanPlayer, AIPlayer
from game.game import Game


def main():
    board = Board()

    
    # ai = MinimaxAI(ai_player="O", human_player="X")

    # p1 = HumanPlayer("X")
    # p2 = AIPlayer("O", ai)



    ai_X = MinimaxAI(ai_player="X", human_player="O")
    ai_O = MinimaxAI(ai_player="O", human_player="X")
    
    p1 = AIPlayer("X", ai_X)
    p2 = AIPlayer("O", ai_O)


    game = Game(board, p1, p2)
    game.play()


if __name__ == "__main__":
    main()