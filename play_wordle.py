from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Enter your guess: ")
        wordle.attempt(x)

        if wordle.is_solved:
            print("Your guess was correct!")
        else:
            print("Your guess was incorrect!")

if __name__ == "__main__":
    main()
