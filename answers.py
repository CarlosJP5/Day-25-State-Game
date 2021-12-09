from turtle import Turtle


class Answer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def correct(self, x_pos, y_pos, guessed):
        self.goto(x_pos, y_pos)
        self.write(guessed)
