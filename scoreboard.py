from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.teleport(0, 260)
        self.show_score()

    def show_score(self):
        self.write(f'{self.l_score}      {self.r_score}', align='center', font=('Courier', 24, 'normal'))

    def up(self, side):
        if side == "right":
            self.r_score += 1
        elif side == "left":
            self.l_score += 1
        self.clear()
        self.show_score()



    def game_over(self, side):
        self.home()
        self.write(f"{side} wins!", align='center',font=('Courier', 24, 'normal'))
