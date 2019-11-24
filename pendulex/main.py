import sys
import pygame

from pendulex import pendulum

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

p = pendulum.Pendulum()
x, y, steps = p.simulate()

i = 0

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                i = 1

    if i < len(steps) - 1:
        i += 1

    magnifier = 100
    offset_x = 400
    offset_y = 40

    current_x = magnifier * (x[i]) + offset_x
    current_x = int(current_x)
    current_y = magnifier * (-y[i]) + offset_y
    current_y = int(current_y)

    start_x = offset_x
    start_y = offset_y

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    pygame.draw.circle(screen, (255, 0, 0), (current_x, current_y), 20)
    pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), (current_x, current_y), 1)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
