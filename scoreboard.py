from turtle import Turtle

with open('high_score.txt') as hs:
    high_score = hs.readline()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Your score: {self.score}. High score: {self.high_score}.", move=False, align='center',
                   font=('Arial', 12, 'normal'))

    def score_up(self):
        self.score += 1
        self.clear()
        self.hs_up()
        self.write(f"Your score: {self.score}. High score: {self.high_score}.", move=False, align='center',
                   font=('Arial', 12, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align='center', font=('Courier', 20, 'normal'), )

    def hs_up(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high_score = open("high_score.txt", "w")
            new_high_score.write(str(self.high_score))
            new_high_score.close()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.hs_up()
        self.write(f"Your score: {self.score}. High score: {self.high_score}.", move=False, align='center',
                   font=('Arial', 12, 'normal'))
