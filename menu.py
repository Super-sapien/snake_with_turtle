import turtle
from turtle import Screen, Turtle
from game_screen import GameOn

# TODO test recursive screen setup * check below
screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake")
screen.tracer(0)
# screen.listen()


class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.snake_logo()
        self.color('white')
        self.play_game()
        self.check_scores()
        self.read_me()
        self.exit()

    def snake_logo(self):
        self.setpos(-130, 190)
        self.color('green')
        self.write("""

█████████████████████████████████
█─▄▄▄▄█▄─▀█▄─▄██▀▄─██▄─█─▄█▄─▄▄─█
█▄▄▄▄─██─█▄▀─███─▀─███─▄▀███─▄█▀█
▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀""")

    def play_game(self):
        self.setpos(-90, 90)
        self.btn_border()
        self.setpos(0, 100)
        self.write(arg=f"Play Game", align="center", font=("Courier", 18, "normal"))

    def check_scores(self):
        self.setpos(-90, -10)
        self.btn_border()
        self.setpos(0, 0)
        self.write(arg=f"Highscores", align="center", font=("Courier", 18, "normal"))

    def read_me(self):
        self.setpos(-90, -110)
        self.btn_border()
        self.setpos(0, -100)
        self.write(arg=f"Read Me", align="center", font=("Courier", 18, "normal"))

    def exit(self):
        self.setpos(-90, -210)
        self.btn_border()
        self.setpos(0, -200)
        self.write(arg=f"Back", align="center", font=("Courier", 18, "normal"))

    def btn_border(self):
        """Draws border around buttons"""
        self.pendown()
        for i in range(2):
            self.forward(180)
            self.left(90)
            self.forward(45)
            self.left(90)
        self.penup()

    def set_about_page(self):
        screen.bgcolor('black')
        self.goto(-235, -40)
        self.write("The concept of Snake originated from the 1976\narcade game Blockade, developed by a British\n"
                   "company called Gremlin Interactive, which shut\ndown in 1984. Blockade was designed as a "
                   "two-\nplayer game in which each would guide their\nown snakes, leaving a solid line behind them.\n"
                   "\n"
                   "This app has been created mostly using the\npython Turtle module. To play, use the arrow\nkeys to "
                   "move up, right, down, and left. Hit Esc\nto pause the game. The game is over if you hit\na "
                   "wall, or your own body. Have fun.",
                   font=('Courier', 12, 'normal'))
        self.back_btn()

    def set_highscore_page(self):
        screen.bgcolor('black')
        self.goto(-235, 0)

        self.back_btn()

    def go_back(self, x, y):
        if (-91 < x < 91) and (-214 < y < -166):
            self.set_up_menu()

    def back_btn(self):
        self.setpos(-90, -210)
        self.btn_border()
        self.exit()
        turtle.onscreenclick(self.go_back, 1)
        turtle.listen()
        turtle.done()

    def button_click(self, x, y):
        """Handles clicks on buttons in main menu for; playing game, checking hiscores, reading about game,
        exiting game respectively."""
        if (-91 < x < 91) and (89 < y < 134):
            self.screen.clear()
            screen.tracer(0)
            GameOn().start_game()

        if (-91 < x < 91) and (-12 < y < 35):
            self.screen.clear()
            screen.tracer(0)
            self.set_highscore_page()

        if (-91 < x < 91) and (-113 < y < -66):
            self.screen.clear()
            screen.tracer(0)
            self.set_about_page()

        if (-91 < x < 91) and (-214 < y < -166):
            Screen().bye()  # exit

    # TODO fix the set_up_menu
    def set_up_menu(self):
        self.screen.clear()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake")
        screen.tracer(0)
        # screen.listen()
        turtle.onscreenclick(menu.button_click, 1)
        Menu()

        # turtle.onscreenclick(menu.button_click, 1)
        # turtle.listen()
        # turtle.done()


menu = Menu()
turtle.listen()
menu.set_up_menu()
turtle.done()
