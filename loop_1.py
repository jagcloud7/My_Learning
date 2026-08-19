#Program to ask the user to find the number 0 (while loop)

print('Lets play a number game')
print('Enter the special number which was invented by an Indian:')

num = int()

while True:
    num = int(input('>'))
    if num > 0:
        print('Try again')
    elif num == 0:
        break
print('Thank you! You have exited the program')