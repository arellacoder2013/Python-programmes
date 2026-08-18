import pygame

def main():
    pygame.init()

    screen_width, screen_height = 700, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mini Sprite Adventure")

    x, y = 60, 60
    sprite_width, sprite_height = 70, 70

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 125, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    PINK = (255, 192, 203)

    current_color = PURPLE

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3

        # Keep the square inside the screen
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        # Change colour when touching an edge
        if x == 0:
            current_color = BLUE
        elif x == screen_width - sprite_width:
            current_color = YELLOW
        elif y == 0:
            current_color = RED
        elif y == screen_height - sprite_height:
            current_color = GREEN
        else:
            current_color = WHITE

        screen.fill(BLACK)

        # Draw shapes
        pygame.draw.circle(screen, GREEN, (420, 320), 35)
        pygame.draw.circle(screen, BLUE, (80, 320), 35, 4)

        pygame.draw.rect(screen, RED, (300, 200, 100, 50))
        pygame.draw.rect(screen, YELLOW, (500, 100, 50, 100), 4)

        pygame.draw.line(screen, PINK, (100, 100), (200, 200), 5)

        # Draw the moving square
        sprite_rect = pygame.Rect(
            x, y, sprite_width, sprite_height
        )

        pygame.draw.rect(screen, current_color, sprite_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
