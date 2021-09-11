# The goal of this program is to greet the user and tell him his age in earth and venus years.

name = input("What is your name? ")  # Uses the users name as an input so we can print it later.
while True:  # Created a loop that loops when the user inputs anything other than a number which would cause an error.

    try:  # It is important that the users uses a number, otherwise it will crash. Try function lets us try the code.
        year_of_birth = int(input("What is your birth year? "))  # Uses users birth year input as an integer.

    except ValueError:  # Detects error and instead of printing error, print message below and loop to start.
        print("Sorry, you can only enter numbers. Please try again.")

    else:  # User has correct input so there is no problem here, we will continue to break.

        break  # This will break the loop and we can continue.


current_year = 2021
user_age = current_year - year_of_birth  # Define user_age by subtracting year of birth from the current year.
earth_venus_ratio = 0.62  # One year on Venus equals 0.62 years on earth.
user_age_venus = user_age / earth_venus_ratio  # Venus age by simply dividing users earth age by the ratio.

# Prints the combined variables and sentence customized to the user input.
print("\nDear " + name + ", in 2021 your age on earth will be " + str(user_age) +
      ". \nAnd your age in Venus years will be " + str(user_age_venus))

# Added this so the user can still be in the window to see the output instead of it exiting immediately.
input("\nPress ENTER to exit")
