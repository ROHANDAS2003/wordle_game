from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random
import os

def main():
    while True:
        os.system('cls')
        print(Fore.BLUE + "\n\n<==== ||_Welcome to Wordle game_|| ====>" + Fore.RESET)
        print("\n\n0. How to play \n1. Play\n2. Exit")
        choice = int(input(":  "))

        if choice == 0:
            os.system('cls')
            print(Fore.BLUE + "\t\tHow to play Wordle:\n\n" + Fore.RESET)
            print("The wordle itself will think of a 5 letter " + Fore.GREEN + "SECRET WORD\n" + Fore.RESET)
            print("You have only " + Fore.BLUE + "6 CHANCE" + Fore.RESET + " to guess that word\n")
            print("Once you guess a word Wordle will provide you some hints on the basis of our guess\n")
            print("\tIf the letter is in word it will highlight it with " + Fore.YELLOW + "YELLO COLOR\n" + Fore.RESET)
            print("\tIf the letter is in word and also in correct place it will highlight it with " + Fore.GREEN + "GREEN COLOR\n" + Fore.RESET)
            print("The word you guess should be a 5 letter valid word containing only english alphabets.\n\n")
            input("Press any key to continue:  ")
        if choice == 1:
            play()
        if choice == 2:
            exit()


def play():
    os.system('cls')
    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    print(f"\nYou have {wordle.remaining_attempts} attempts remaining.")

    while wordle.can_attempt:
        x = input(Fore.BLUE + "\nType your guess:  " + Fore.RESET)
        x = x.upper()

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!" + Fore.RESET)
            continue

        if not x.isalpha():
            print(Fore.RED + "word should only contain alphabetic letters." + Fore.RESET)
            continue

        if not x in word_set:
            print(Fore.RED + f"{x} is not a valid word!" + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)
        
    if wordle.is_solved:
        print("\nYou've solved the puzzle.\n")

        again = input("Want to play agian [y/n]:  ")

        if again == "y" or again == "yes":
            play()
        else:
            exit()
    else:
        print("\nYou failed to solve the puzzle!")
        print("The secret word was: " + Fore.GREEN + f"{wordle.secret}\n" + Fore.RESET)

        again = input("Want to play agian [y/n]:  ")

        if again == "y" or again == "yes":
            play()
        else:
            exit()


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def display_results(wordle: Wordle):
    print("Your results so far...")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)

    print(f"You have {wordle.remaining_attempts} attempts remaining.")


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)



def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):

    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)


if __name__ == "__main__":
    main()
