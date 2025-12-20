"""Check if a year is a leap year using only if."""
year = 2024
if year % 400 ==0 or year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
