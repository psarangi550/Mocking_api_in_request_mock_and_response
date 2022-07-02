import random 

def roll_dice():
    print("Rolling dice...")
    return random.randint(1,6)


def guess_number(num):
    result=roll_dice()
    if result == num: 
        return "You Won"
    else:
        return "You Lost"



