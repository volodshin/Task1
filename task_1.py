def is_year_leap():
    year = int(input("Введіть рік: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_year_leap())
