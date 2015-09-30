"""http://www.informatik.uni-rostock.de/~nl/files/loi/aufgaben/blatt1.pdf"""
"""Exercise 2"""

"""def print_result(ly_result):"""

year = input("Please enter a year: ")

if year % 4 != 0:
    print year, ("is no leap year")
else:
    if year % 100 == 0 and year % 400 != 0:
            print year, ("is a leap year")
    elif year % 100 == 0:
            print year, ("is no leap year")
    else:
            print year, ("is a leap year")
