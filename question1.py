def to_ic(number):
    # Convert the number to string
    num_str = str(number)
    
    # Split the number into integer and decimal parts
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
    else:
        integer_part, decimal_part = num_str, ''

    # Reverse the integer part to process from the last digit
    reversed_integer = integer_part[::-1]

    # Initialize result list to store the formatted digits
    result = []

    # Add the first three digits
    result.append(reversed_integer[:3])
    
    # Add the rest of the digits in pairs
    for i in range(3, len(reversed_integer), 2):
        result.append(reversed_integer[i:i+2])
    
    # Join the parts with commas and reverse back
    formatted_integer = ','.join(result)[::-1]
    
    # If there is a decimal part, add it to the formatted integer part
    if decimal_part:
        return formatted_integer + '.' + decimal_part
    else:
        return formatted_integer

# Test the function
print(to_ic(504678))  # Output: 5,04,678
print(to_ic(12345678))  # Output: 1,23,45,678
print(to_ic(12345))  # Output: 12,345
print(to_ic(123))  # Output: 123
