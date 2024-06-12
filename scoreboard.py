from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!",align="center", font=FONT)
    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left",font=FONT)

    def increase_score(self):
        self.score += 1
