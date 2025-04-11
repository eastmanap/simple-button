import pygame
import sys
import colors
from config import *

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen

def handle_events(button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_button(screen, rect, color):
    pygame.draw.rect(screen, color, rect)

def draw_text(screen, font, text, color, center_pos):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=center_pos)
    screen.blit(surf, rect)

def main():
    screen = init_game()
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('Arial', 45, bold=False)
    button_length = 150
    button_width = 60
    button_x = 300
    button_y = 275
    button = pygame.Rect(button_x, button_y, button_length, button_width)

    running = True
    while running:
        running = handle_events(button)
        screen.fill(colors.WHITE)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button.collidepoint(mouse_x, mouse_y):
            button_color = colors.WEIRDLY_SATURATED_SKY_BLUE
            button_length = 170
            button_width = 80
            button_x = 290
            button_y = 265
            font = pygame.font.SysFont('Arial', 55, bold=True)
        else:
            button_color = colors.YOUTUBE_AD_RED
            button_length = 150
            button_width = 60
            button_x = 300
            button_y = 275
            font = pygame.font.SysFont('Arial', 45, bold=False)

        button = pygame.Rect(button_x, button_y, button_length, button_width)
        draw_button(screen, button, button_color)
        draw_text(screen, font, 'Exit?', colors.BLACK, button.center)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
