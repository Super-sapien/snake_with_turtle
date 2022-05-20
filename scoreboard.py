from turtle import Turtle, Screen
import tkinter as tk

screen = Screen()
canvas = screen.cv


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        data.close()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(0, 260)
        self.write(arg=f"Score: {self.score} Hiscore: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def new_high_score(self):
        print("in new hs")
        self.setpos(0, 25)
        self.write(f"  New High score!\nType your initials", align="center", font=("Courier", 18, "normal"))
 # TODO make input box submit
        canvas.create_window(0, 20, tags=["entry"], window=tk.Entry())

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            # TODO add ability to type initials (3 letters) assign to highscore
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.update_scoreboard()

    def reset_game(self):
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Courier", 18, "normal"))
        self.setpos(0, -40)
        self.write(arg=f"Press 'a' to play again", align="center", font=("Courier", 18, "normal"))

