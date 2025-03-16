# Write a program to check if a given year is a leap year. A year is a leap year if it is divisible by 4 but not divisible by 100,
# or it is divisible by 400. Implement the logic using nested if statement.
year = int(input("Enter a year: "))

if year % 4 == 0:  # Divisible by 4
    if year % 100 == 0:  # Divisible by 100
        if year % 400 == 0:  # Divisible by 400
            print(f"{year} is a leap year.")  # Special case for years divisible by 400
        else:
            print(f"{year} is not a leap year.")  # Divisible by 100 but not by 400
    else:
        print(f"{year} is a leap year.")  # Divisible by 4 but not by 100
else:
    print(f"{year} is not a leap year.")