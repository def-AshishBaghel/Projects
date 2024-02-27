import pygame
import random
import time
pygame.init()

time.sleep(5)


game_score = 0
fps = 10
screen_x = 600
screen_y = 600

screen_color = (2, 30, 66)
snake_color = (255, 255, 255)
food_color = (250, 246, 27)
score_color = (0, 255, 0)
snake_x = 120
snake_y = 120
snake_size = 15
snake_speed_x = 20
snake_speed_y = 0
food_x = random.randint(50, 450)
food_y = random.randint(50, 450)
score_x = 20
score_y = 20

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Snake Game")
pygame.display.update()

game_quit = False
game_clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
final_text = font.render("Score: " + str(game_score), True, score_color)

snake_list = []
snake_length = 1

def draw_snake(window, color, snake_list, snake_size):
    for segment in snake_list:
        pygame.draw.rect(window, color, (segment[0], segment[1], snake_size, snake_size))

game_over = False

def display_text(screen_text, color, x, y):
    font = pygame.font.SysFont(None, 35)
    text = font.render(screen_text, True, color)
    screen.blit(text, (x, y))

while not game_quit:
    if game_over:
        screen.fill(screen_color)
        display_text("Hello! I am Ashish Baghel And ", snake_color, 20, 100)
        display_text("I have Created this game using Python-pygame", snake_color, 20, 150)
        display_text("Game Over! Press Enter To Continue", snake_color, 20, 200)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False
                    snake_x = 120
                    snake_y = 120
                    snake_speed_x = 20
                    snake_speed_y = 0
                    game_score = 0
                    snake_length = 1
                    snake_list.clear()
                    food_x = random.randint(50, 450)
                    food_y = random.randint(50, 450)
                    final_text = font.render("Score: " + str(game_score), True, score_color)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed_y == 0:
                    snake_speed_x = 0
                    snake_speed_y = -20
                if event.key == pygame.K_DOWN and snake_speed_y == 0:
                    snake_speed_x = 0
                    snake_speed_y = 20
                if event.key == pygame.K_RIGHT and snake_speed_x == 0:
                    snake_speed_x = 20
                    snake_speed_y = 0
                if event.key == pygame.K_LEFT and snake_speed_x == 0:
                    snake_speed_x = -20
                    snake_speed_y = 0

        snake_x += snake_speed_x
        snake_y += snake_speed_y

        distance = ((snake_x - food_x) ** 2 + (snake_y - food_y) ** 2) ** 0.5
        if distance < snake_size:
            food_x = random.randint(50, 450)
            food_y = random.randint(50, 450)
            game_score += 10
            final_text = font.render("Score: " + str(game_score), True, score_color)
            snake_length += 1

        head = [snake_x, snake_y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == head:
                game_over = True

        if snake_x >= screen_x or snake_y >= screen_y or snake_x < 0 or snake_y < 0:
            game_over = True

        screen.fill(screen_color)
        draw_snake(screen, snake_color, snake_list, snake_size)
        screen.blit(final_text, (score_x, score_y))
        pygame.draw.rect(screen, food_color, (food_x, food_y, snake_size, snake_size))
        pygame.display.update()
        game_clock.tick(fps)


pygame.quit()
