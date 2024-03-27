import sys

def input_year():
    global year
    year = int(sys.stdin.readline())

def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0

def result():
    input_year()
    res = leap_year(year)
    print(res)

result()
