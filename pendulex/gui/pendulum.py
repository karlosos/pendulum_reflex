import pygame


class Pendulum:
    def __init__(self):
        self.colors = [(0, 227, 11), (227, 198, 0), (226, 144, 0), (181, 38, 10)]

    def draw(self, screen, x, y, intensity):
        magnifier = 100
        offset_x = 400
        offset_y = 40

        current_x = magnifier * (x) + offset_x
        current_x = int(current_x)
        current_y = magnifier * (-y) + offset_y
        current_y = int(current_y)

        start_x = offset_x
        start_y = offset_y

        pygame.draw.circle(screen, self.colors[intensity], (current_x, current_y), 20)
        pygame.draw.line(screen, self.colors[intensity], (start_x, start_y), (current_x, current_y), 1)
