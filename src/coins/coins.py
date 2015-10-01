"""
http://www.informatik.uni-rostock.de/~nl/files/loi/aufgaben/blatt1.pdf
Exercise 4
"""

# Definitions
coins_options_list = [200, 100, 50, 10, 5, 2, 1]


def enter_request():
    """Request input"""
    amount = float(input("Enter an amount to pay: ")) * 100
    return amount


def calculate_resultset(amount):
    """Calculate needed coins"""
    i = 0
    coins_result_list = []
    while amount >= 0.01:
        coins_result_list.append(amount // coins_options_list[i])
        amount -= coins_options_list[i] * coins_result_list[i]
        i += 1
    return coins_result_list


def print_result(coins_result_list):
    """Assemble result sentence and print"""
    coins_total = 0
    for i in coins_result_list:
        coins_total += i
    print("You need at least"), int(coins_total), "coins!"


print_result(calculate_resultset(enter_request()))


