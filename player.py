import csv

class Player:
    def __init__(self, name):
        self.name = name #can't be edited in game
        self.score = 0
        self.high_score = 0

        with open("score/score.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if self.name == row[0]:
                    self.high_score = int(row[1])

    def  __str__(self):
        return f"  player: {self.name}   current score: {self.score}   high score: {self.high_score} "

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,n):
        self._name = n

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,s):
        self._score = s

    @property
    def high_score(self):
        return self._high_score
    @high_score.setter
    def high_score(self,h):
        self._high_score = h