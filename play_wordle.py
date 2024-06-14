from wordle import Wordle
from letter_state import LetterState
from colorama import Fore

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("\nEnter your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Your guess must be {wordle.WORD_LENGTH} characters long." + Fore.RESET)
            continue
        wordle.attempt(x)
        display_results(wordle)

        if wordle.is_solved:
            print("\nYour guess was correct!")
        else:
            print("\nYour guess was incorrect!")

def display_results(wordle: Wordle):
    print(f"\nYou have {wordle.remaining_attempts} attempts remaining.")
    print("Your results so far ...\n")
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        print(" ".join(["_"] * wordle.WORD_LENGTH))

def convert_result_to_color(result: list[LetterState]):
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

if __name__ == "__main__":
    main()
