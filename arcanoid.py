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
GRIS = (155, 155, 155)
Color = [(255, 0, 255), (0, 0, 255), (200, 200, 0), (100,100,100), (20,200,20), (200, 20, 100), (240, 100, 231), (4, 250, 34), (255, 148, 4)]  # Lista de colores

# Velocidad de la pelota
BALL_SPEED = 4

# Dimensiones de la paleta
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Dimensiones de los bloques
BLOCK_WIDTH = 67
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLUMNS = 14

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
        self.image.fill(GRIS)
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

# Clase para los bloques
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(random.choice(Color))  # Seleccionar un color aleatorio de la lista
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Función principal del juego
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Arkanoid")

    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    paddle = Paddle()
    ball = Ball()

    all_sprites.add(paddle)
    all_sprites.add(ball)

    for row in range(BLOCK_ROWS):
        for column in range(BLOCK_COLUMNS):
            block = Block(BLOCK_WIDTH * column + 5, BLOCK_HEIGHT * row + 50)
            blocks.add(block)
            all_sprites.add(block)

    clock = pygame.time.Clock()
    running = True

    score = 0
    font = pygame.font.Font(None, 36)

    game_over_font = pygame.font.Font(None, 50)
    game_over_text = game_over_font.render("Game Over", True, WHITE)  # Definición aquí
    restart_text = font.render("Presione R para reinciar", True, WHITE)  # Definición aquí

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not ball.alive():
                    main()  # Reiniciar el juego

        if len(blocks) > 0:
            all_sprites.update()

            # Colisiones con los bloques
            block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
            for block in block_hit_list:
                score += 10
                ball.dy = -ball.dy

            # Colisión con la paleta
            if pygame.sprite.collide_rect(ball, paddle):
                ball.dy = -ball.dy

            screen.fill((255, 255, 255))
            all_sprites.draw(screen)

            # Mostrar puntaje
            score_text = font.render("Score: " + str(score), True, WHITE)
            screen.blit(score_text, [SCREEN_WIDTH - 150, 10])
        else:
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50))

        # Verificar si la pelota ha alcanzado el fondo de la pantalla
        if not ball.alive() and len(blocks) > 0:
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()




