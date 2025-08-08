import random

"""
This is the simple choice engine. the first part of the Stat engine. Its a simple python script that takes
in user inputs for what they want, also takes in a scale.

Goal; to simulate a dice role where you can cheat based on how much you want something.
The more choices you enter, the more heads the dice gets!

basically a choice engine for indecisive people (like me!)
s
"""

def get_wants():
    wants = []
    print("Enter what you 'want' as a choice and how much you want them (1–10 scale). Type 'done' to finish.\n")
    while True:
        name = input("Enter a 'choice' (or type 'done' to exit): ") ## declare name variable for choices
        if name.lower() == 'done':
            break
        try:
            weight = int(input(f"How much do you want '{name}'? (1-10): "))
            wants.append((name, weight))
        except ValueError:
            print("Please enter a valid number.")
    return wants

def pick_choice(choices):
    names = [c[0] for c in choices]
    weights = [c[1] for c in choices]
    
    return random.choices(names, weights=weights, k=1)[0]

def main():
    print(" Welcome to the Choice Machine !")
    choices = get_wants()
    if not choices:
        print("No wants provided. Exiting.")
        return
    print("\nRolling the dice...\n")
    result = pick_choice(choices)
    print(f"Your choice is: {result}")

if __name__ == "__main__":
    main()
