import random

choice= input("want to roll dice?[y/n]")
roll_history = [ ]
score = 0
roll_count = 0
while choice.lower() == "y":
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("""
===============
🎲 DICE ROLLER
===============""")
    print(f"\n🎲 Dice 1: {dice1}")
    print(f"🎲 Dice 2: {dice2}")
    roll_history.append((dice1,dice2))

    total = dice1 + dice2
    score += total
    roll_count += 1
    print(f"\n➕ Total: {total}")
    print(f"🏆 Score: {score}")
    print(f"🔁 Rolls: {roll_count}")

    print("\n📜 Roll history")
    print("---------------")
    for i, roll in enumerate(roll_history, start=1):
        print(f"{i}. {roll}")

    if total == 7:
        print()
        print("🍀 Lucky Number : Yes")
    else:
        print()
        print("🍀 Lucky Number : No")
    print()
    choice = input("🎲 Roll again?[y/n]: ")

if choice.lower() == "n":
    print("Why not?your loss😐")

else:
    print("Please enter either 'y' or 'n'")
