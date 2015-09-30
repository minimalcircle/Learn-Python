"""http://www.informatik.uni-rostock.de/~nl/files/loi/aufgaben/blatt1.pdf"""
"""Exercise 4"""

# Definitions
coins_options_list = [200, 100, 50, 10, 5, 2, 1]
coins_result_list = []
i = 0

# User Interaction
amount = input("Enter an amount to pay: ") * 100

# Calculation
while amount >= 0.01:
    coins_result_list.append(amount // coins_options_list[i])
    amount -= coins_options_list[i] * coins_result_list[i]
    i += 1

# Show Results
coins_total = 0
for i in coins_result_list:
    coins_total += i
print ("You need at least"), int(coins_total), ("coins!")
