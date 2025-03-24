from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', 'r') as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 20, "bold"))
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('high_score.txt', 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()