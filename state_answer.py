from turtle import Turtle
FONT = ("Arial", 8, "normal")
BIG_FONT = ("Arial", 80, "normal")

class StateAnswer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()

    def pup_up(self, state_name, position):
        self.goto(position)
        self.write(state_name, align="center", font=FONT)

    def you_win(self):
        self.goto(0, -50)
        self.color("orange")
        self.write("You Win!", align="center", font=BIG_FONT)

    def bye(self):
        self.goto(0, -50)
        self.color("orange")
        self.write("Good-Bye!", align="center", font=BIG_FONT)
