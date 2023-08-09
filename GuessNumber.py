import random


def generate_random_number(num_digits):
    """
    Generate a random number with the given number of digits.
    """
    min_num = 10 ** (num_digits - 1)
    max_num = (10 ** num_digits) - 1
    return random.randint(min_num, max_num)


def is_even(number):
    """
    Check if a number is even.
    """
    return number % 2 == 0


def get_num_digits(level):
    """
    Get the number of digits based on the chosen level (easy/medium/hard).
    """
    ranges = {"A": (3, 4), "B": (5, 6), "C": (7, 9)}
    return random.randint(*ranges[level])


def get_user_guess(num_digits):
    """
    Ask the user for their guess and return the entered number.
    """
    while True:
        try:
            user_guess = input(f"Enter your guess ({num_digits} digits): ")
            if len(user_guess) != num_digits or not user_guess.isdigit():
                print(f"Please enter {num_digits} digits.")
            else:
                return int(user_guess)
        except ValueError:
            print("Please enter an integer.")


def count_matching_digits(secret_number, user_guess):
    """
    Count the number of digits in the user's guess that match the secret number.
    """
    return sum(1 for digit in str(user_guess) if digit in str(secret_number))


def count_matching_positions(secret_number, user_guess):
    """
    Count the number of digits in the user's guess that match both value and position in the secret number.
    """
    return sum(1 for a, b in zip(str(secret_number), str(user_guess)) if a == b)


def main():
    print("Choose difficulty level:")
    print("A - Easy (3-4 digits)")
    print("B - Medium (5-6 digits)")
    print("C - Hard (7-9 digits)")

    while True:
        level = input("Enter your choice (A/B/C): ").upper()
        if level in ("A", "B", "C"):
            break
        else:
            print("Please choose a valid level (A/B/C).")

    num_digits = get_num_digits(level)
    secret_number = generate_random_number(num_digits)
    print(f"The number has {num_digits} digits and is {'even' if is_even(secret_number) else 'odd'}.")

    hints = 0
    attempts = 0
    user_guesses = []

    while attempts < 10:
        attempts += 1
        user_guess = get_user_guess(num_digits)
        user_guesses.append(user_guess)

        print("Your entered guesses:")
        for guess in user_guesses:
            print(guess)

        matching_digits = count_matching_digits(secret_number, user_guess)
        print(f"Matching digits: {matching_digits}")

        matching_positions = count_matching_positions(secret_number, user_guess)
        if matching_positions == num_digits:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif matching_positions > 0:
            print(f"Digits in correct positions: {matching_positions}")

        if attempts == 7:
            answer = input("You have made 7 guesses without success. Do you want to end? (Y/N): ").upper()
            if answer == "Y":
                print(f"The random number is: {secret_number}")
                break

        if attempts == 10:
            answer = input("You have made 10 guesses without success. Do you want to use a hint? (Y/N): ").upper()
            if answer == "Y":
                hints += 1
                if hints <= 4:  # Limit the number of hints
                    matching_positions = count_matching_positions(secret_number, user_guess)
                    matching_positions_digits = [a for a, b in zip(str(secret_number), str(user_guess)) if a == b and str(secret_number).index(a) == str(user_guess).index(b)]
                    print(f"Hint {hints}: Digits in correct positions: {', '.join(matching_positions_digits)}")
                else:
                    print("You have used all available hints.")
            else:
                continue

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "Y":
        main()
    else:
        print("Thank you for playing. Goodbye!")


if __name__ == "__main__":
    main()