import random # using the random library from the pythons standard libraries 
              # https://docs.python.org/3/library/random.html#random.choices

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

    # example for choices: choices = [("Pizza", 10), ("Salad", 2), ("Gym", 5)]
    
    names = []   # List to store the names of the choices
    weights = [] # List to store how much you want each choice

    for item in choices:
        name = item[0]      # First part of the tuple (e.g. "Pizza")
        weight = item[1]    # Second part of the tuple (e.g. 10)
        names.append(name)
        weights.append(weight)
    
    return random.choices(names, weights=weights, k=1)[0]
    # Return a k sized list of elements chosen from the population with replacement. 
    # If the relative weights are specified, the selection probability for each element is proportional 
    # to its weight.

"""
The random function picks random elements with "replacement"
    replacement: you can pick the same thing more than once
"""


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
