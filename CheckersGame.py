# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 03/02/2023
# Description: For this project you will write a class called Checkers that allows two people to play
# the game of Checkers. This is a variation of the original Checkers game with modified rules.
class OutofTurn(Exception):
    """Raises exception if a player attempts to move out of turn."""
    pass


class InvalidSquare(Exception):
    """Raises an exception if a player attempts to move a piece that is not theirs or if the square does
    not exist."""
    pass


class InvalidPlayer(Exception):
    """Raises an exception if the player's name is not valid."""
    pass


class Player:
    """Represents a player in a Checkers game."""
    def __init__(self, player_name, piece_color):
        self.player_name = player_name
        self.piece_color = piece_color
        self.king_count = 0
        self.triple_king_count = 0
        self.captured_pieces_count = 0

    def get_king_count(self):
        """Returns the number of kings the player has on the board."""
        return self.king_count

    def get_triple_king_count(self):
        """Returns the number of triple kings the player has on the board."""
        return self.triple_king_count

    def get_captured_pieces_count(self):
        """Returns the number of captured pieces."""
        return self.captured_pieces_count


class Checkers:
    """Represents a Checkers game as played."""
    def __init__(self):
        self.board = [[None, "White", None, "White", None, "White", None, "White"],
                      ["White", None, "White", None, "White", None, "White", None],
                      [None, "White", None, "White", None, "White", None, "White"],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      ["Black", None, "Black", None, "Black", None, "Black", None],
                      [None, "Black", None, "Black", None, "Black", None, "Black"],
                      ["Black", None, "Black", None, "Black", None, "Black", None]]
        self.player1 = None
        self.player2 = None

    def create_player(self, player_name, piece_color):
        """Creates a specific player and their piece color."""
        if self.player1 is None:
            self.player1 = Player(player_name, piece_color)
            return self.player1
        else:
            self.player2 = Player(player_name, piece_color)
            return self.player2

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Creates a new game of Checkers."""
        if player_name == self.player1.player_name:
            cur_player = self.player1
            other_player = self.player2
        elif player_name == self.player2.player_name:
            cur_player = self.player2
            other_player = self.player1
        else:
            raise InvalidPlayer

        x0, y0 = starting_square_location
        x1, y1 = destination_square_location

        if x0 < 0 or x0 > 7 or y0 < 0 or y0 > 7 or x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7:
            raise InvalidSquare

        if self.board[x0][y0] != cur_player.piece_color:
            raise InvalidSquare

        if self.board[x1][y1] is not None:
            raise InvalidSquare

        if abs(x1 - x0) > 2 or abs(y1 - y0) > 2:
            raise InvalidSquare

        captured_piece_count = 0

        if abs(x1 - x0) == 2 and abs(y1 - y0) == 2:
            captured_x = (x0 + x1) // 2
            captured_y = (y0 + y1) // 2

            if self.board[captured_x][captured_y] == other_player.piece_color or self.board[captured_x][captured_y] == other_player.piece_color + "_king":
                self.board[captured_x][captured_y] = None
                captured_piece_count = 1

                if other_player.piece_color == "Black":
                    other_player.captured_pieces_count += 1
                else:
                    other_player.captured_pieces_count += 1

        if x1 == 0 and cur_player.piece_color == "White":
            self.board[x1][y1] = "White_king"
            cur_player.king_count += 1
        elif x1 == 7 and cur_player.piece_color == "Black":
            self.board[x1][y1] = "Black_king"
            cur_player.king_count += 1

        if x1 == 0 and cur_player.piece_color == "White" and x0 == 7:
            self.board[x1][y1] = "White_triple_king"
            cur_player.triple_king_count += 1
        elif x1 == 7 and cur_player.piece_color == "Black" and x0 == 0:
            self.board[x1][y1] = "Black_triple_king"
            cur_player.triple_king_count += 1

        self.board[x0][y0] = None
        self.board[x1][y1] = cur_player.piece_color

        return captured_piece_count

    def get_checker_details(self, square_location):
        """Returns whether is piece is on the square and if it's a valid square for a move."""
        x, y = square_location

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise InvalidSquare

        return self.board[x][y]

    def print_board(self):
        """Prints the current board."""
        for row in self.board:
            print(row)

    def game_winner(self):
        """Returns whether the game has been won and by whom."""
        if self.player1.captured_pieces_count == 12:
            return self.player2.player_name
        elif self.player2.captured_pieces_count == 12:
            return self.player1.player_name
        else:
            return "Game has not ended"
