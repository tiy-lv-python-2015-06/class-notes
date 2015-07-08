import random

class Game:
    """
     Should print instructions
     Create and start the turn
     Adding turn score to player score
     End game when player reaches 100
    """
    def __init__(self, player1, player2):
        self.die = Die()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def start(self):
        while not self.winner():
            turn = Turn(self.current_player, self.die)
            turn.run()
            self.current_player.score += turn.score
            print("{}'s score is now {}".format(self.current_player,
                                            self.current_player.score))
            self.switch_player()

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def winner(self):
        if self.player1.score < 100 and self.player2.score < 100:
            return None

        if self.player1 >= 100:
            return self.player1
        else:
            return self.player2

class Turn:
    """
    Roll the die
    Record result
    Tell the player result
    Ask the player to roll again
    """

    def __init__(self, player, die):
        self.score = 0
        self.player = player
        self.turn_over = False
        self.die = die

    def record_roll(self, roll):
        if roll == 1:
            self.turn_over = True
            self.score = 0
        else:
            self.score += roll

    def run(self):
        while not self.turn_over:
            self.go()

    def go(self):
        roll = self.die.roll()
        self.record_roll(roll)
        self.player.record_roll(roll)
        print("{} you rolled a {} and your turn score is {}".format(self.player.name, roll, self.score))
        if not self.turn_over:
            self.turn_over = not self.player.go_again()



class Player:
    """ Should decide whether to go again """

    def __init__(self, name="Bob"):
        self.name = name
        self._score = 0
        self.rolls = []

    def record_roll(self, roll):
        self.rolls.append(roll)

    def go_again(self):
        answer = input("Roll again?").lower()
        if answer[0] == 'y':
            return True
        else:
            return False

    def __str__(self):
        return "Player: {}".format(self.name)


class ComputerPlayer(Player):

    def go_again(self):
        return False

class Die:
    def roll(self):
        return random.randint(1,6)

if __name__ == '__main__':
    player1 = Player("Frodo")
    player2 = ComputerPlayer("Sam")

    game = Game(player1, player2)
    game.start()