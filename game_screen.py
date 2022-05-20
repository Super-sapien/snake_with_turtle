from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from pause_menu import PauseMenu
import time


class GameOn:
    def __init__(self):
        self.game_on = False
        self.game_over = False
        self.score_board = Scoreboard()  # TODO check is this bad practice?

    def toggle_pause(self):
        self.game_on = not self.game_on

    def start_game(self):
        print('game start')
        self.game_on = True
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake")
        screen.tracer(0)
        snake = Snake()
        snake.reset_snake()
        food = Food()
        # scoreboard = Scoreboard()
        pause_screen = PauseMenu()

        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(self.toggle_pause, "Escape")

        while not self.game_over:
            screen.update()

            if self.game_on:
                pause_screen.clear_pause_screen()
                time.sleep(0.1)
                snake.move()

                # Detect collision with walls
                if snake.head.xcor() > 280 or snake.head.xcor() < -305 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
                    # self.score_board.game_over()
                    self.game_over = True

                # Detect collision with food
                if snake.head.distance(food) < 15:
                    food.refresh()
                    snake.extend()
                    self.score_board.increase_score()

                # Detect collision with tail
                for segment in snake.snake[1:]:
                    if snake.head.distance(segment) < 10:
                        # self.score_board.game_over()
                        self.game_over = True

            # Display Pause menu TODO make pause screen run once instead of in while loop
            else:
                pause_screen.set_pause_screen()

        if self.game_over:
            if self.score_board.score > self.score_board.high_score:
                print('new highscore!!')
                self.score_board.new_high_score()

            with open("data.txt") as data:
                self.score_board.high_score = int(data.read())
            # TODO make game-over message appear only if not asking for high score submission
            # self.score_board.game_over()
            screen.onkey(self.new_game, 'a')
            # screen.onkey(Screen().bye(), 'Esc')
            print('game over')

    def new_game(self):
        print('game reset')
        Screen().clear()
        Screen().tracer(0)
        self.score_board.reset_game()
        self.game_over = False
        self.start_game()



