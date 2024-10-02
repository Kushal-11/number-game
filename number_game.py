import random

def generate_number():
    return random.randint(1000, 9999)

def hide_digit(num):
    # hide a random digit and replace it with underscore
    num_of_digits = len(str(num))
    hidden_index = random.randint(0, num_of_digits - 1)
    hidden_digit = int(str(num)[hidden_index])
    num_str = str(num)
    num_str = num_str[:hidden_index] + "_" + num_str[hidden_index + 1:]

    return num_str, hidden_digit

def guess_digit(num_str, hidden_digit):
    tries = 3
    while tries > 0:
        print(f"Guess the hidden digit in {num_str}")
        guess = input()
        if guess == str(hidden_digit):
            print("Congratulations! You guessed it right!")
            break
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")
    else:
        print(f"Sorry! The hidden digit was {hidden_digit}")

    print("Do you want to play again? (y/n)")
    choice = input().lower()
    if choice == "n":
        print("Goodbye!")
        exit()
    else:
        start_game()

def start_game():
    num1 = generate_number()
    num2 = generate_number()

    print("First number:", num1)
    print("Second number:", num2)
    ans = num1 * num2

    num_str, hidden_digit = hide_digit(ans)
    print(num_str)
    guess_digit(num_str, hidden_digit)


if __name__ == "__main__":
    print("Two 4-digit numbers are multiplied and one of the digits will be hidden. Guess the hidden digit in three tries.")
    print("Are you ready? (y/n)")
    ready = input().lower()
    if ready == "n":
        print("Goodbye!")
        exit()
    else:
        start_game()