import math

class MinimaxAI:
    def __init__(self, ai_player="O", human_player="X"):
        self.ai = ai_player
        self.human = human_player

    def evaluate(self, winner):
        if winner == self.ai:
            return 1
        elif winner == self.human:
            return -1
        return 0

    def minimax(self, board, is_max):
        winner = board.check_winner()

        if winner is not None:
            return self.evaluate(winner)

        if is_max:
            best = -math.inf
            for move in board.available_moves():
                board.make_move(move, self.ai)
                score = self.minimax(board, False)
                board.undo_move(move)
                best = max(best, score)
            return best
        else:
            best = math.inf
            for move in board.available_moves():
                board.make_move(move, self.human)
                score = self.minimax(board, True)
                board.undo_move(move)
                best = min(best, score)
            return best

    def best_move(self, board):
        best_score = -math.inf
        move = None

        for m in board.available_moves():
            board.make_move(m, self.ai)
            score = self.minimax(board, False)
            board.undo_move(m)

            if score > best_score:
                best_score = score
                move = m

        return move