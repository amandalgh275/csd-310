#!/usr/bin/env python3
"""
bottles.py

Prompt the user for how many bottles of beer are on the wall, pass that
number into a countdown function that prints the verses while counting
down to 1, uses "bottle" singular when appropriate, and returns to
main to remind the user to buy more beer.
"""

def countdown(n: int) -> None:
    """
    Count down from n to 1, printing the song verses.
    Uses correct singular/plural forms for "bottle".
    """
    for i in range(n, 0, -1):
        current_word = "bottle" if i == 1 else "bottles"
        next_count = i - 1

        if next_count == 1:
            next_phrase = "1 bottle of beer on the wall."
        elif next_count == 0:
            next_phrase = "no more bottles of beer on the wall."
        else:
            next_phrase = f"{next_count} bottles of beer on the wall."

        print(f"{i} {current_word} of beer on the wall, {i} {current_word} of beer.")
        print("Take one down, pass it around,")
        print(next_phrase)
        print()  # blank line between verses

def get_positive_int(prompt: str = "Enter number of bottles: ") -> int:
    """
    Prompt until the user enters a valid integer >= 1.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            print("Please enter an integer greater than or equal to 1.")
        except ValueError:
            print("That's not a valid integer. Please try again.")

def main() -> None:
    n = get_positive_int()
    countdown(n)
    print("Time to buy more bottles of beer.")

if __name__ == "__main__":
    main()