import unittest
from CheckersGame import Checkers, InvalidSquare, InvalidPlayer


class TestCheckers(unittest.TestCase):
    def setUp(self):
        """Creates two players for tests."""
        self.game = Checkers()
        self.player1 = self.game.create_player("Adam", "White")
        self.player2 = self.game.create_player("Lucy", "Black")

    def test_play_game_invalid_square(self):
        """Tests the InvalidSquare exception."""
        with self.assertRaises(InvalidSquare):
            self.game.play_game("Lucy", (5, 6), (8, 7))

    def test_play_game_invalid_player(self):
        """Tests the InvalidPlayer exception."""
        with self.assertRaises(InvalidPlayer):
            self.game.play_game("John", (2, 1), (3, 0))

    def test_get_checker_details(self):
        """Tests the return on the details of a checker square."""
        self.assertEqual(self.game.get_checker_details((1, 2)), "White")
        self.assertEqual(self.game.get_checker_details((6, 1)), "Black")

    def test_get_checker_details_invalid_square(self):
        """Tests the InvalidSquare exception."""
        with self.assertRaises(InvalidSquare):
            self.game.get_checker_details((8, 2))

    def test_game_winner_not_ended(self):
        """Tests the return of the game_winner function."""
        self.assertEqual(self.game.game_winner(), "Game has not ended")


if __name__ == '__main__':
    unittest.main()
