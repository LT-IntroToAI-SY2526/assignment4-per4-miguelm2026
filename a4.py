# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        """Initialize an empty board."""
        self.board = ["*"] * 9

    def __str__(self):
        """Return a formatted string representation of the board."""
        rows = []
        for i in range(0, 9, 3):
            rows.append(" ".join(self.board[i:i+3]))
        return "\n".join(rows)

    def make_move(self, player, pos):
        """Attempt to make a move for a player at position pos.

        Args:
            player: 'X' or 'O'
            pos: int from 0–8

        Returns:
            True if move successful, False otherwise
        """
        if player not in ["X", "O"]:
            return False
        if not (0 <= pos < 9):
            return False
        if self.board[pos] != "*":
            return False
        self.board[pos] = player
        return True

    def has_won(self, player):
        """Return True if the player has won the game."""
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_positions:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def game_over(self):
        """Return True if the game is over (win or full board)."""
        if self.has_won("X") or self.has_won("O"):
            return True
        if "*" not in self.board:
            return True
        return False

    def clear(self):
        """Reset the board to the starting state."""
        self.board = ["*"] * 9


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise"""
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # Basic tests
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!\n")

    # Automatically start the interactive game
    play_tic_tac_toe()