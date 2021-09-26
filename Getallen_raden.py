import random

# Initial variables, set to none and 0 each game.
user_guess = None
chance_count = 0

# Variable users input. Also used to determine the maximum and minimum of the random number.
lower_number = int(input("Please select a minimum number: "))
higher_number = int(input("Please select a maximum number: "))
chances = int(input("How many chances would you like? "))
random_number = random.randint(lower_number, higher_number)

# Created a list that tracks the guesses and if it was higher or lower. We will join them later on
numberList = []
higher_or_lowerList = []

# Loop to check if user input is between 1 and 5. If not, prints an error message and user has to try again.
while True:
    if chances > 5 or chances < 1:
        print("Error! Please select a value between 1 and 5! ")
        chances = int(input("How many chances would you like? "))
    elif chances > 1 or chances < 5:
        break

# First asks the user for a random number, then appends it to the list we created and ads a +1 to the chance counter.
# It then loops until you either lose by reaching the max chances or when u win.
# Also gives tips when the number is higher or lower than the random secret number.
while user_guess != random_number:
    user_guess = int(input(f"Please enter a number between {lower_number} and {higher_number}: "))
    numberList.append(user_guess)
    chance_count += 1

    if user_guess == random_number:
        print(f"\nWell done! Your guess is correct! Below u can find a list of your guesses.\n")
        break

    elif user_guess > random_number:
        higher_or_lowerList.append("Too high")
        print("\nYour guess is too high! Please try again: ")

    elif user_guess < random_number:
        higher_or_lowerList.append("Too low")
        print("\nYour guess is too low! Please try again: ")

    if chance_count == chances:
        print(f"\nYou're out of chances, you lose! \n The random number was {random_number}, "
              f"below u can find a list of your guesses.\n")
        break

print("Your guess   Too high or too low.")

# Loop to access each item by index so we can print both lists we stored which are the user guesses and high/low
for i in range(len(higher_or_lowerList)):
    print(f"{numberList[i]} \t\t\t {higher_or_lowerList[i]}")


input("Press ENTER to exit")
