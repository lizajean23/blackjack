class Player:
    def __init__(self, name, score=0, turn=0, answer="yes"):
        self.name = name
        self.score = score
        self.turn = turn
        self.answer = answer

    def __str__(self):
        return f'welcome to lizJACK{self.name},your current score:{self.score}'


class Game:

    def __init__(self, player1, player2, winner="IT IS A TIE"):
        self.player1 = player1
        self.player2 = player2
        self.winner = winner

    def __str__(self):
        return f'this game was between {self.player1.name} and {self.player2.name}, won by {self.winner} '

    def play(self):

        import random
        self.player1.turn = random.randint(1, 12)
        self.player2.turn = random.randint(1, 12)
        # აქ 11 რო ამოვიდეს და აგებინებდეს ეგ თამაშს ერთი უნდა გახდეს ეგეც არვიცი როგორ
        while True:
            if self.player1.answer == "yes":
                question_1 = input(
                    f"{self.player1.name} you have {self.player1.turn} in sum, do you want to add?\nyes or no : ")
            if self.player2.answer == "yes":
                question_2 = input(
                    f"{self.player2.name} you have {self.player2.turn} in sum, do you want to add?\nyes or no : ")
            
            if question_1 == "yes":
                self.player1.turn += random.randint(1, 12)
            if question_2 == "yes":
                self.player2.turn += random.randint(1, 12)
# es perebi jobs
            elif question_1 == "no" and question_2 == "no":
                break

            if question_1 == "no":
                self.player1.answer = "no"
            if question_2 == "no":
                self.player2.answer = "no"

            if self.player1.turn >= 21 or self.player2.turn >= 21:
                break

        if self.player1.turn > 21:
            if self.player1.turn < self.player2.turn:
                self.winner = self.player1.name
                self.player1.score += 1
            elif self.player1.turn > self.player2.turn:
                self.winner = self.player2.name
                self.player2.score += 1

        elif self.player2.turn > 21:
            if self.player2.turn < self.player1.turn:
                self.winner = self.player2.name
                self.player2.score += 1
            elif self.player2.turn > self.player1.turn:
                self.winner = self.player1.name
                self.player1.score += 1

        elif self.player1.turn < 21:
            if self.player2.turn > 21:
                self.winner = self.player1.name
                self.player1.score += 1
            elif self.player2.turn == 21:
                self.winner = self.player2.name
                self.player2.score += 1

        elif self.player2.turn < 21:
            if self.player1.turn > 21:
                self.winner = self.player2.name
                self.player2.score += 1
            elif self.player1.turn == 21:
                self.winner = self.player1.name
                self.player1.score += 1

        elif self.player2.turn < 21 and self.player1.turn < 21:
            if self.player1.turn > self.player2.turn:
                self.winner = self.player1.name
                self.player1.score += 1
            elif self.player2.turn > self.player1.turn:
                self.winner = self.player2.name
                self.player2.score += 1

        elif self.player1.turn == self.player2.turn:
            self.winner = "IT WAS A TIE"

        print(self.player1.turn)
        print(self.player2.turn)
        # print(self.winner)


p1 = Player('ლულ')
p2 = Player('liziko')
game1 = Game(p1, p2)

game1.play()
print(game1)
print(p1.score)
print(p2.score)