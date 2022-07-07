

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculation():
    num1 = float(input("What is the first number?: "))
    calculator_off = False
    while not calculator_off:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter the operation")
        num2 = float(input("What is the second number?: "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Do you want to continue calculation ? 'y' for continue with {answer} or 'n' for new calculation") == "y":
            num1 = answer
        else:
            calculator_off = True
            calculation()


calculation()

