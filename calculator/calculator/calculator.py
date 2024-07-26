from logo import art  # Import the art from the logo module


# Define basic arithmetic functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary to map operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


def calculator():
    """
    Function to perform a sequence of arithmetic operations.
    """
    print(art)  # Display the calculator art
    num1 = float(input("Enter the first number: "))  # Get the first number

    # Display available operations
    for operator in operations:
        print(operator)

    should_continue = True  # Control variable for the main loop

    while should_continue:
        # Get the operation symbol from the user
        operation_symbol = input("Pick an operation symbol from the line above: ")

        # Get the second number
        num2 = float(input("Enter the second number: "))

        # Retrieve the appropriate function from the dictionary and calculate the result
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")  # Display the result

        # Ask the user if they want to continue or start a new calculation
        want_continue = input(
            "Type 'yes' to continue calculating, 'no' to start a new calculation, or 'exit' to leave: ").lower()
        if want_continue == "yes":
            num1 = answer  # Use the previous answer as the new first number
        elif want_continue == "no":
            calculator()  # Restart the calculator
        elif want_continue == "exit":
            should_continue = False  # Exit the loop and end the calculator


# Start the calculator
calculator()
