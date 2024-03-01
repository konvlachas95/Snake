from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, align=ALIGN, font=FONT)

    def update_score(self):
        self.write(f"Score : {self.score}", False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

