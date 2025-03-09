import random


class Game:
    CHOICES = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

    def __init__(self):
        self.computer_pick = ""
        self.user_pick = ""

    def get_compter_choice(self):
        """Function to return computer's choice"""
        key = random.randint(1, 3)
        return self.CHOICES[key]

    def get_user_choice(self):

        while True:
            choice = input("Enter your choice: Rock/Paper/Scissors:\t").upper()

            if choice in (self.CHOICES.values()):
                break
            else:
                print("Invalid choice!")
                continue

        return choice

    def get_result(self):
        if self.computer_pick == self.user_pick:
            return -1

        elif self.user_pick == "PAPER" and self.computer_pick == "ROCK":
            return 1
        elif self.user_pick == "ROCK" and self.computer_pick == "SCISSORS":
            return 1
        elif self.user_pick == "SCISSORS" and self.computer_pick == "PAPER":
            return 1
        else:
            return 0

    def play(self):
        self.computer_pick = self.get_compter_choice()
        self.user_pick = game.get_user_choice()

        result = self.get_result()

        print("Computer Choice: ", self.computer_pick)
        print("Your Choice: ", self.user_pick)

        if result == 1:
            print("You win 😋")
        if result == 0:
            print("You lose 🥹")
        if result == -1:
            print("Draw 🥲")


while True:
    game = Game()
    game.play()

    play_again = input("Do you want to play again? y/n:\t")
    print("-----------------------------------------------\n")
    if play_again.lower() != "y":
        break
