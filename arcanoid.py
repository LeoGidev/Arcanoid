import pygame
import random
# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Velocidad de la pelota
BALL_SPEED = 5

# Dimensiones de la paleta
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Dimensiones de los bloques
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10

# Clase para la paleta
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# Clase para la pelota
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.dx = BALL_SPEED * random.choice([-1, 1])
        self.dy = BALL_SPEED * random.choice([-1, 1])

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.dx = -self.dx

        if self.rect.top <= 0:
            self.dy = -self.dy

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()