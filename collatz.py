# The Collatz Sequence Exercise

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        # Print the number followed by a space instead of a new line
        print(result, end=' ') 
        return result
    else:
        result = 3 * number + 1
        print(result, end=' ')
        return result

# 1. Input Validation: Try to get a valid integer from the user
try:
    print('Enter number:')
    user_input = input('>')
    
    # Convert input to an integer
    current_number = int(user_input)
    
    # Print the starting number on the same line if desired
    print(current_number, end=' ')
    
    # 2. The Loop: Keep calling collatz() until current_number becomes 1
    while current_number != 1:
        current_number = collatz(current_number)
        
    print() # Prints a final new line when the sequence finishes

except ValueError:
    # This runs if int() fails (e.g., if the user types 'puppy')
    print('Error: You must enter an integer.')