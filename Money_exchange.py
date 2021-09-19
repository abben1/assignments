# Below is a simple money exchange for the US dollar, GB pounds and Japanese Yen, output is in Euro

# Link user input to variable
currency = int(input("Currency (1 = US dollar, 2 = GB pounds, 3 = Yen): "))
user_amount = int(input("Amount to exchange: "))

# Variable declaration
transaction_rate = 0.015
transaction_cost = float(round(user_amount * transaction_rate, 2))
usd_exchange_rate = 0.85
gbp_exchange_rate = 1.17
yen_exchange_rate = 0.0078

# Loops through transaction cost, and sets a minimum and maximum price a customer has to pay (2 and 15 euro)
if transaction_cost < 2:
    transaction_cost = 2
elif transaction_cost > 15:
    transaction_cost = 15

# Loop of three print functions depending on the selected currency. Output is rounded to 2 decimals.
if currency == 1:
    print(f"For {user_amount} USD you will get {round(user_amount * usd_exchange_rate, 2)} Euro. "
          f"The transaction costs are {transaction_cost}. "
          f"You will receive {round(user_amount * usd_exchange_rate - transaction_cost, 2)}")
elif currency == 2:
    print(f"For {user_amount} GBP you will get {round(user_amount * gbp_exchange_rate, 2)} Euro. "
          f"The transaction costs are {transaction_cost}. "
          f"You will receive {round(user_amount * gbp_exchange_rate - transaction_cost, 2)}")
elif currency == 3:
    print(f"For {user_amount} Yen you will get {round(user_amount * yen_exchange_rate, 2)} Euro. "
          f"The transaction costs are {transaction_cost}. "
          f"You will receive {round(user_amount * yen_exchange_rate - transaction_cost, 2)}")
