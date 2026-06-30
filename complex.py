import pygame
import numpy as np
from math import sin, cos

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Julia Fractal")

clock = pygame.time.Clock()

x = np.linspace(-1.8, 1.8, WIDTH)
y = np.linspace(-1.4, 1.4, HEIGHT)
X, Y = np.meshgrid(x, y)

frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = frame * 0.01
    c = complex(
        0.7885 * cos(t * 0.7),
        0.7885 * sin(t * 0.5)
    )

    Z = X + 1j * Y
    M = np.full(Z.shape, True, dtype=bool)
    output = np.zeros(Z.shape)

    for i in range(80):
        Z[M] = Z[M] ** 2 + c
        escaped = np.abs(Z) > 4
        output[escaped & M] = i
        M &= ~escaped

    colors = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    colors[:, :, 0] = (output * 9 + frame) % 255
    colors[:, :, 1] = (output * 5 + frame * 2) % 255
    colors[:, :, 2] = (output * 13 + frame * 3) % 255

    surface = pygame.surfarray.make_surface(colors.swapaxes(0, 1))
    screen.blit(surface, (0, 0))

    pygame.display.flip()

    frame += 1
    clock.tick(30)

pygame.quit()