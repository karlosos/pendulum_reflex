import pygame

from . import pendulum


class Display:
    def __init__(self, game):
        self.__game = game
        pygame.init()

        size = width, height = 800, 600

        self.screen = pygame.display.set_mode(size)
        self.pend = pendulum.Pendulum()

    def show(self, x, y, intensity, score, player_name, score_board):
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))

        self.pend.draw(self.screen, x, y, intensity)
        font = pygame.font.SysFont("Times New Roman", 18)
        score_disp = font.render(f"Score: {score}", 1, (0, 0, 0))
        self.draw_score_board_game(self.screen, player_name, score_board, player_score=score)
        self.screen.blit(score_disp, (650, 50))
        pygame.display.flip()

    def draw_score_board_game(self, screen, player_name, score_board, player_score):
        better = score_board[0]
        worse = score_board[1]

        idx = 0
        font = pygame.font.SysFont("Times New Roman", 18)
        for idx, score in enumerate(better):
            score_name_disp = font.render(f"{score[0]}", 1, (0, 0, 0))
            score_disp = font.render(f"{score[1]}", 1, (0, 0, 0))
            self.screen.blit(score_name_disp, (650, 75 + (idx*15)))
            self.screen.blit(score_disp, (710, 75 + (idx*15)))

        score_name_disp = font.render(f"{player_name}", 1, (0, 0, 0))
        score_disp = font.render(f"{player_score}", 1, (255, 0, 0))
        self.screen.blit(score_name_disp, (650, 75 + ((idx+1) * 15)))
        self.screen.blit(score_disp, (710, 75 + ((idx+1) * 15)))

        for idx2, score in enumerate(worse):
            score_name_disp = font.render(f"{score[0]}", 1, (0, 0, 0))
            score_disp = font.render(f"{score[1]}", 1, (0, 0, 0))
            self.screen.blit(score_name_disp, (650, 75 + ((idx + idx2 + 2) * 15)))
            self.screen.blit(score_disp, (710, 75 + ((idx + idx2 + 2) * 15)))

    def draw_score_board_pause(self, screen, score_board):
        font = pygame.font.SysFont("Times New Roman", 30)
        for idx, score in enumerate(score_board):
            score_name_disp = font.render(f"{score[0]}", 1, (0, 0, 0))
            score_disp = font.render(f"{score[1]}", 1, (0, 0, 0))
            self.screen.blit(score_name_disp, (340, 230 + (idx*30)))
            self.screen.blit(score_disp, (440, 230 + (idx*30)))

    def show_end_game(self, score_board):
        font = pygame.font.SysFont("Times New Roman", 30)
        end_game = font.render(f"End game", 1, (0, 0, 0))
        self.screen.blit(end_game, (350, 150))
        font = pygame.font.SysFont("Times New Roman", 20)
        end_game_info = font.render(f"Press enter", 1, (0, 0, 0))
        self.screen.blit(end_game_info, (365, 190))
        self.draw_score_board_pause(self.screen, score_board)
        pygame.display.flip()

    def show_menu(self, player_name, score_board):
        background = pygame.Surface(self.screen.get_size())
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))
        font = pygame.font.SysFont("Times New Roman", 30)
        for idx, character in enumerate(player_name):
            char_disp = font.render(f"{character}", 1, (0, 0, 0))
            self.screen.blit(char_disp, (355 + (idx * 30), 150))

        font = pygame.font.SysFont("Times New Roman", 30)
        for i in range(5):
            char_disp = font.render(f"_", 1, (0, 0, 0))
            self.screen.blit(char_disp, (355 + (i * 30), 150))

        self.draw_score_board_pause(self.screen, score_board)
        pygame.display.flip()

