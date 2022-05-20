from turtle import Turtle


class PauseMenu(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def set_pause_screen(self):
        self.penup()
        self.hideturtle()
        self.snake_logo()
        self.color('white')
        self.goto(-125, 0)
        self.write("Press Esc to Resume", font=('Courier', 18, 'normal'))

    def snake_logo(self):
        self.setpos(-150, 150)
        self.color('green')
        self.write("""
        
██████████████████████████████████████
█▄─▄▄─██▀▄─██▄─██─▄█─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
██─▄▄▄██─▀─███─██─██▄▄▄▄─██─▄█▀██─██─█
▀▄▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀
""")

    def clear_pause_screen(self):
        self.clear()
