from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.move_speed = 0.1

    def game_over(self):
        self.goto(0, 0);
        self.write("GAME OVER", False, "center", FONT)

    def increment_score(self):
        self.clear()
        self.score += 1
        self.goto(-210, 250)
        self.write(f"Level: {self.score}", False, "center", FONT)
        self.move_speed *= 0.7