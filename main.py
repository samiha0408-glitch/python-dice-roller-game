import random

choice= input("want to roll dice?[y/n]")
score = 0
roll_count = 0
while choice.lower() == "y":
    print("Rolling dice...")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"({dice1},{dice2})")

    total = dice1 + dice2
    score += total
    roll_count += 1
    print(f"Total: {total}")
    print(f"score: {score}")
    print(f"rolls: {roll_count}")
    if total == 7:
        print("congratulations! you rolled the lucky numbr🥳")
    else:
        print("not so lucky today!")

    choice = input("want to roll again?[y/n]")

if choice.lower() == "n":
    print("Why not?your loss😐")

else:
    print("Please enter either 'y' or 'n'")
