import pygame
import sys
import random
import numpy as np

from pendulex.simulation import pendulum
from pendulex import gui
from pendulex import trigger_object
from pendulex import score_board


class Game:
    def __init__(self):
        self.p = pendulum.Pendulum()
        self.score_board = score_board.ScoreBoard()
        self.clock = pygame.time.Clock()
        self.display = gui.display.Display(self)
        x, y, steps = self.p.simulate()
        self.simulation = {"x": x, "y": y, "theta": self.p.theta1, "steps": steps}

        self.i = 0
        self.moving_right = False
        self.objects_list = []
        self.intensity = 0
        self.score = 0
        self.tours = 1
        self.game_state = 0
        self.player_name = ""

    def clear_game(self):
        self.i = 0
        self.moving_right = False
        self.objects_list = []
        self.intensity = 0
        self.score = 0
        self.tours = 1
        self.game_state = 0
        self.player_name = ""

    def loop(self):
        while 1:
            if self.game_state == 0:
                self.events_menu()
                self.menu()
            elif self.game_state == 1:
                self.events_game()
                self.game()
            elif self.game_state == 2:
                self.events_end_game()
                self.display.show_end_game(self.score_board.get_score_board_full())
            self.clock.tick(60)

    def menu(self):
        self.display.show_menu(self.player_name, self.score_board.get_score_board_full())

    def game(self):
        if self.i < len(self.simulation["steps"]) - 1:
            self.i += 1

        self.check_angle_activation()
        x = self.simulation["x"][self.i]
        y = self.simulation["y"][self.i]
        theta = self.simulation["theta"][self.i]

        for o in self.objects_list:
            if theta < o.theta and self.moving_right:
                self.intensity += o.action()
            elif theta > o.theta and not self.moving_right:
                self.intensity += o.action()

        self.score += self.intensity
        self.display.show(x, y, self.intensity, self.normalized_score(), self.player_name,
                          self.score_board.get_score_board_split(self.normalized_score()))
        if self.tours > 7:
            self.game_state = 2
            self.score_board.add_score(self.player_name, self.normalized_score())

    def normalized_score(self):
        return round(self.score / self.tours, 2)

    def reset_time(self):
        self.i = 0

    def check_angle_activation(self):
        theta = self.simulation["theta"][self.i]
        if theta > 1.10 and not self.moving_right:
            self.tours += 1
            self.moving_right = not self.moving_right
            self.clear_trigger_objects()
            self.generate_trigger_objects()
        if theta < -1.10 and self.moving_right:
            self.tours += 1
            self.moving_right = not self.moving_right
            self.clear_trigger_objects()
            self.generate_trigger_objects()

    def generate_trigger_objects(self):
        random_thetas = random.sample(range(-90, 90, 20), 3)
        random_thetas = np.array(random_thetas)/100
        for theta in random_thetas:
            self.objects_list.append(trigger_object.TriggerObject(theta))

    def clear_trigger_objects(self):
        print("Clearing objects and adding penalty")
        self.intensity = 0
        self.objects_list = []

    def player_action(self):
        if self.intensity > 0:
            self.intensity = 0
        else:
            theta = self.simulation["theta"][self.i]
            if -1.10 < theta < 1.10:
                self.score += 10

    def events_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.teardown()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player_action()

    def events_menu(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.teardown()

            if evt.type == pygame.KEYDOWN:
                if evt.unicode.isalpha():
                    if len(self.player_name) < 5:
                        self.player_name += evt.unicode
                    else:
                        new_name = list(self.player_name)
                        new_name[4] = evt.unicode
                        self.player_name = ''.join(new_name)
                elif evt.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                elif evt.key == pygame.K_RETURN:
                    self.game_state = 1

    def events_end_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.teardown()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_state = 0
                    self.clear_game()

    def teardown(self):
        self.score_board.save_scores()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.loop()