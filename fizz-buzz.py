print("WELCOME TO THE FIZZBUZZ")
num = int(input("Select the number upto which you want to calculate.\n"))

for number in range(1, num + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

