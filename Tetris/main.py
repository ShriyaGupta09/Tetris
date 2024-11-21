import sys
import pygame
from game import Game
from color import Colors

pygame.init()

# Font setup
title_font = pygame.font.Font(None, 38)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Rectangles for displaying score and next block
score_rect = pygame.Rect(424, 55, 170, 60)
next_rect = pygame.Rect(424, 215, 170, 180)

screen = pygame.display.set_mode((660, 720))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()

        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.black)

    screen.fill(Colors.black)

    # Draw the background rectangles first
    pygame.draw.rect(screen, Colors.saffron, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.saffron, next_rect, 0, 10)

    # Draw the static text
    screen.blit(score_surface, (470, 20))
    screen.blit(next_surface, (480, 180))

    # Draw the game over text if needed
    if game.game_over:
        screen.blit(game_over_surface, (430, 450))

    # Draw the dynamic score value on top of the score rectangle
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                  centery=score_rect.centery))

    # Draw the game elements (blocks, grid)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
