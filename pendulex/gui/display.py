import pygame

from . import pendulum


class Display:
    def __init__(self, game):
        self.__game = game
        pygame.init()

        size = width, height = 800, 600

        self.screen = pygame.display.set_mode(size)
        self.pend = pendulum.Pendulum()

    def show(self, x, y, intensity, score):
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))

        self.pend.draw(self.screen, x, y, intensity)
        font = pygame.font.SysFont("Times New Roman", 18)
        score = font.render(f"Score: {score}", 1, (0, 0, 0))
        self.screen.blit(score, (650, 50))
        pygame.display.flip()

    def show_end_game(self):
        font = pygame.font.SysFont("Times New Roman", 30)
        end_game = font.render(f"End game", 1, (0, 0, 0))
        self.screen.blit(end_game, (350, 250))
        font = pygame.font.SysFont("Times New Roman", 20)
        end_game_info = font.render(f"Press enter", 1, (0, 0, 0))
        self.screen.blit(end_game_info, (365, 290))
        pygame.display.flip()

    def show_menu(self, player_name):
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))
        font = pygame.font.SysFont("Times New Roman", 30)
        for idx, character in enumerate(player_name):
            char_disp = font.render(f"{character}", 1, (0, 0, 0))
            self.screen.blit(char_disp, (355 + (idx * 30), 250))

        font = pygame.font.SysFont("Times New Roman", 30)
        for i in range(5):
            char_disp = font.render(f"_", 1, (0, 0, 0))
            self.screen.blit(char_disp, (355 + (i * 30), 250))

        pygame.display.flip()

