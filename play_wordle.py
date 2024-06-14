from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Enter your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(f"Your guess must be {wordle.WORD_LENGTH} characters long.")
            continue
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")

        if wordle.is_solved:
            print("Your guess was correct!")
        else:
            print("Your guess was incorrect!")

if __name__ == "__main__":
    main()
