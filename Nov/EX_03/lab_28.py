def calculator():
    """Accept 3 inputs and perform basic arithmetic operations."""

    try:
        # Accept 3 inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        # Perform addition
        addition = num1 + num2 + num3
        print(f"\nAddition: {num1} + {num2} + {num3} = {addition}")

        # Perform subtraction
        subtraction = num1 - num2 - num3
        print(f"Subtraction: {num1} - {num2} - {num3} = {subtraction}")

        # Perform multiplication
        multiplication = num1 * num2 * num3
        print(f"Multiplication: {num1} × {num2} × {num3} = {multiplication}")

        # Perform division (check for division by zero)
        if num2 != 0 and num3 != 0:
            division = num1 / num2 / num3
            print(f"Division: {num1} ÷ {num2} ÷ {num3} = {division}")
        else:
            print(f"Division: Cannot divide by zero!")
            if num2 == 0:
                print(f"  Error: Second number is zero")
            if num3 == 0:
                print(f"  Error: Third number is zero")

        # Return results as a dictionary
        results = {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division if num2 != 0 and num3 != 0 else None
        }

        return results

    except ValueError:
        print("Error: Please enter valid numbers!")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    print("=" * 50)
    print("Calculator with 3 Inputs")
    print("=" * 50)
    calculator()