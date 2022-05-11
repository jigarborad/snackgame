from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.goto(x=0, y=280)
        self.speed("fastest")
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()
        else:
            self.score = 0
            self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", False, align='center', font=('Arial', 16, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High score: {self.high_score}", False, align='center', font=('Arial', 12,
                                                                                                       'normal'))

    def score_count(self):
        self.score += 1
        self.update_scoreboard()
