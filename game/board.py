class Board:
    def __init__(self):
        self.state = [" "] * 9

    def available_moves(self):
        return [i for i, v in enumerate(self.state) if v == " "]

    def make_move(self, position, player):
        if self.state[position] == " ":
            self.state[position] = player
            return True
        return False

    def undo_move(self, position):
        self.state[position] = " "

    def check_winner(self):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a, b, c in combos:
            if self.state[a] == self.state[b] == self.state[c] and self.state[a] != " ":
                return self.state[a]

        if " " not in self.state:
            return "Empate"

        return None

    def print(self):
        print()
        for i in range(0, 9, 3):
            print(self.state[i], "|", self.state[i+1], "|", self.state[i+2])
        print()