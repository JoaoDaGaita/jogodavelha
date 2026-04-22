class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.p1 = player1
        self.p2 = player2
        self.current = player1

    def switch_player(self):
        self.current = self.p1 if self.current == self.p2 else self.p2

    def play(self):
        while True:
            self.board.print()

            move = self.current.get_move(self.board)
            self.board.make_move(move, self.current.symbol)

            winner = self.board.check_winner()
            if winner:
                self.board.print()
                if winner == "Empate":
                    print("Empate!")
                else:
                    print(f"{winner} venceu!")
                break

            self.switch_player()