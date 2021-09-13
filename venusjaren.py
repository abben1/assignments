# The goal of this program is to greet the user and tell him his age in earth and venus years.

# Uses the users name as an input so we can print it later.
name = input("What is your name? ")

# Created a loop that loops when the user inputs anything other than a number which would cause an error.
# It is important that the users uses a number, otherwise it will crash. Try function lets us try the code.
# Detects error and instead of printing error, print message below and loop to start until user enters a number
while True:
    try:
        year_of_birth = int(input("What is your birth year? "))
    except ValueError:
        print("Sorry, you can only enter numbers. Please try again.")
    else:
        break

# Variable declaration
current_year = 2021
user_age = current_year - year_of_birth
earth_venus_ratio = 0.62

# calculation
user_age_venus = user_age / earth_venus_ratio

# Prints the combined variables and sentence customized to the user input.
print(f"\nDear {name}, in 2021 your age on earth will be {user_age}. "
      f"\nAnd your age in Venus years will be {user_age_venus}.")

# Added this so the user can still be in the window to see the output instead of it exiting immediately.
input("\nPress ENTER to exit")
