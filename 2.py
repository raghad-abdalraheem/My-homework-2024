def binary_to_decimal(binary_str):
    try:
        # Convert binary string to decimal number
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        # Handle cases where input is not a valid binary number
        return None
def main():
    while True:
        # Get binary number input from user
        binary_str = input("Enter a binary number: ")
        # Convert to decimal
        decimal_number = binary_to_decimal(binary_str)
        if decimal_number is not None:
            # If conversion is successful, display the result
            print(f"The decimal equivalent of binary {binary_str} is {decimal_number}.")
            break
        else:
            # If conversion fails, display an error message and prompt again
            print("Invalid binary number. Please enter a valid binary number (only 0 and 1).")
if _name_ == "_main_":
    main()
