import pygame
import random

# Initialize the pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
dis_width = 800
dis_height = 600

class SnakeGame:
    def __init__(self):
        self.dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake_block = 10
        self.snake_speed = 15
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)

        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.game_close = False
        self.x1 = dis_width / 2
        self.y1 = dis_height / 2
        self.x1_change = 0
        self.y1_change = 0
        self.snake_list = []
        self.length_of_snake = 1
        self.generate_food()
        self.obstacles = [
            (100, 100), (200, 200), (300, 300), (400, 400),
            (500, 100), (600, 200), (700, 300)
        ]

    def generate_food(self):
        self.foodx = round(random.randrange(0, dis_width - self.snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, dis_height - self.snake_block) / 10.0) * 10.0

    def check_collision_with_borders(self):
        return self.x1 >= dis_width or self.x1 < 0 or self.y1 >= dis_height or self.y1 < 0

    def check_collision_with_self(self):
        return any(segment == [self.x1, self.y1] for segment in self.snake_list[:-1])

    def check_collision_with_obstacles(self):
        return [self.x1, self.y1] in self.obstacles

    def update_snake(self):
        self.snake_list.append([self.x1, self.y1])
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

    def check_if_eaten_food(self):
        if self.x1 == self.foodx and self.y1 == self.foody:
            self.length_of_snake += 1
            self.generate_food()

    def draw_elements(self):
        self.dis.fill(blue)
        # Draw the fruit
        pygame.draw.rect(self.dis, green, [self.foodx, self.foody, self.snake_block, self.snake_block])
        # Draw obstacles
        for obs in self.obstacles:
            pygame.draw.rect(self.dis, red, [obs[0], obs[1], self.snake_block, self.snake_block])
        # Draw the snake
        for segment in self.snake_list:
            pygame.draw.rect(self.dis, black, [segment[0], segment[1], self.snake_block, self.snake_block])

    def game_loop(self):
        while not self.game_over:
            while self.game_close:
                self.dis.fill(blue)
                self.display_message("You Lost! Press Q-Quit or C-Play Again", red)
                self.display_score(self.length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.reset_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_block
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -self.snake_block
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = self.snake_block
                        self.x1_change = 0

            if self.check_collision_with_borders():
                self.game_close = True

            self.x1 += self.x1_change
            self.y1 += self.y1_change

            self.update_snake()
            self.check_if_eaten_food()

            if self.check_collision_with_self() or self.check_collision_with_obstacles():
                self.game_close = True

            self.draw_elements()
            self.display_score(self.length_of_snake - 1)

            pygame.display.update()
            self.clock.tick(self.snake_speed)

        pygame.quit()

    def display_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, yellow)
        self.dis.blit(value, [0, 0])

    def display_message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Start the game
if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()
