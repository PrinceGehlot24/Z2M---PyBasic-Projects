def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(p, month):
    if month > 12 or month < 1:
        return "Invalid month "
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(p) and month == 2:
        return 29
    else:
        return month_days[month - 1]


x = int(input("YEAR"))
y = int(input("MONTH"))
days = days_in_month(x, y)
print(days)


