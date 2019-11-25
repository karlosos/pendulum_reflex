import csv


class ScoreBoard:
    def __init__(self):
        self.scores = []
        self.load_scores()

    def load_scores(self):
        with open('scores.txt', newline='') as scores_file:
            score_reader = csv.reader(scores_file, delimiter=',', quotechar='|')
            for row in score_reader:
                self.scores.append((row[0], float(row[1])))

    def get_score_board_full(self):
        sorted_by_score = sorted(self.scores, key=lambda score: score[1])
        return sorted_by_score

    def get_score_board_split(self, player_score):
        sorted_by_score = sorted(self.scores, key=lambda score: score[1])
        scores_better = list(filter(lambda s: s[1] < player_score, sorted_by_score))
        scores_worse = list(filter(lambda s: s[1] > player_score, sorted_by_score))
        return scores_better, scores_worse

    def add_score(self, name, score):
        self.scores.append((name, score))

    def save_scores(self):
        with open('scores.txt', 'w', newline='') as scores_file:
            score_writer = csv.writer(scores_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for score in self.scores:
                score_writer.writerow(score)
