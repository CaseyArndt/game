from game import coin_game, coin_game_dp
import unittest

class CoinGameTestCase(unittest.TestCase):
    def test1(self):
        arr = [10, 100, 50, 10]
        expected = 110
        self.assertEqual(coin_game(arr), expected)
    
    def test2(self):
        arr = [50, 50, 100, 100]
        expected = 150
        self.assertEqual(coin_game(arr), expected)

    def test3(self):
        arr = [10, 10, 90, 20]
        expected = 100
        self.assertEqual(coin_game(arr), expected)

    def test4(self):
        arr = [10, 20, 20, 10]
        expected = 30
        self.assertEqual(coin_game(arr), expected)

    def test5(self):
        arr = [10, 10, 60, 50]
        expected = 70
        self.assertEqual(coin_game(arr), expected)

    def test6(self):
        arr = [5, 10, 50, 50, 25, 40, 90, 20] # 5, 90, 25, 50
        expected = 170
        self.assertEqual(coin_game(arr), expected)

    def test7(self):
        arr = [10, 10]
        expected = 10
        self.assertEqual(coin_game(arr), expected)

    def test8(self):
        arr = [10, 20]
        expected = 20
        self.assertEqual(coin_game(arr), expected)

    def test9(self):
        arr = [0, 0]
        expected = 0
        self.assertEqual(coin_game(arr), expected)

    def test10(self):
        arr = [10, 50, 90, 60, 80, 20, 5, 60] # 60, 5, 80, 90
        expected = 235
        self.assertEqual(coin_game(arr), expected)

    def test11(self):
        arr = [90, 80, 10, 40, 10, 90] # 90, 80, 40
        expected = 210
        self.assertEqual(coin_game(arr), expected)

    def test12(self):
        arr = [5, 10, 15, 90, 5, 1] # 1, 10, 90 
        expected = 101
        self.assertEqual(coin_game(arr), expected)


class CoinGameDPTestCase(unittest.TestCase):
    def test1(self):
        arr = [10, 100, 50, 10]
        expected = 110
        self.assertEqual(coin_game_dp(arr), expected)
    
    def test2(self):
        arr = [50, 50, 100, 100]
        expected = 150
        self.assertEqual(coin_game_dp(arr), expected)

    def test3(self):
        arr = [10, 10, 90, 20]
        expected = 100
        self.assertEqual(coin_game_dp(arr), expected)

    def test4(self):
        arr = [10, 20, 20, 10]
        expected = 30
        self.assertEqual(coin_game_dp(arr), expected)

    def test5(self):
        arr = [10, 10, 60, 50]
        expected = 70
        self.assertEqual(coin_game_dp(arr), expected)

    def test6(self):
        arr = [5, 10, 50, 50, 25, 40, 90, 20] # 5, 90, 25, 50
        expected = 170
        self.assertEqual(coin_game_dp(arr), expected)

    def test7(self):
        arr = [10, 10]
        expected = 10
        self.assertEqual(coin_game_dp(arr), expected)

    def test8(self):
        arr = [10, 20]
        expected = 20
        self.assertEqual(coin_game_dp(arr), expected)

    def test9(self):
        arr = [0, 0]
        expected = 0
        self.assertEqual(coin_game_dp(arr), expected)

    def test10(self):
        arr = [10, 50, 90, 60, 80, 20, 5, 60] # 60, 5, 80, 90
        expected = 235
        self.assertEqual(coin_game_dp(arr), expected)

    def test11(self):
        arr = [90, 80, 10, 40, 10, 90] # 90, 80, 40
        expected = 210
        self.assertEqual(coin_game_dp(arr), expected)

    def test12(self):
        arr = [5, 10, 15, 90, 5, 1] # 1, 10, 90 
        expected = 101
        self.assertEqual(coin_game(arr), expected)


if __name__ == '__main__':
    unittest.main()
