import unittest
from snake_game import SnakeGame

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = SnakeGame()

    def test_food_spawn(self):
        food_position = (self.game.foodx, self.game.foody)
        self.assertTrue(0 <= food_position[0] < 800)
        self.assertTrue(0 <= food_position[1] < 600)

    def test_initial_snake_length(self):
        self.assertEqual(self.game.length_of_snake, 1)

    def test_snake_growth(self):
        initial_length = self.game.length_of_snake
        self.game.x1 = self.game.foodx
        self.game.y1 = self.game.foody
        self.game.check_if_eaten_food()
        self.assertEqual(self.game.length_of_snake, initial_length + 1)

    def test_collision_with_borders(self):
        self.game.x1 = 801
        self.assertTrue(self.game.check_collision_with_borders())
        self.game.x1 = -1
        self.assertTrue(self.game.check_collision_with_borders())
        self.game.y1 = 601
        self.assertTrue(self.game.check_collision_with_borders())
        self.game.y1 = -1
        self.assertTrue(self.game.check_collision_with_borders())

    def test_collision_with_self(self):
        self.game.snake_list = [[self.game.x1, self.game.y1], [self.game.x1 - 10, self.game.y1]]
        self.assertTrue(self.game.check_collision_with_self())
        self.game.snake_list = [[self.game.x1 + 10, self.game.y1]]
        self.assertFalse(self.game.check_collision_with_self())

    def test_collision_with_obstacles(self):
        self.game.x1, self.game.y1 = self.game.obstacles[0]
        
        self.assertFalse(self.game.check_collision_with_obstacles())

if __name__ == '__main__':
    unittest.main()
