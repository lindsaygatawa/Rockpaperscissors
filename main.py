import random

def lets_play():
    user = input("Whats your choice? ""R for rock,P for paper, S for scissors: ")
    computer = random.choice(["R", "P", "S"])

    """Rules to determine who wins"""
    if user == computer:
        return "it's a tie!"

    if is_win(user, computer):
        return "Yey, you won!"

    return "You lost!!"


def is_win(player, opponent):
    if (player == "R" and opponent == "S") or (player == "S" and opponent == "P") or (player == "P" and opponent == "R"):
        return True

print(lets_play())



