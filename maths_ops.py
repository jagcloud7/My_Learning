# This is an exercise program for funtion call

def even_odd(num):
    
    if num % 2 == 0:
        num = num // 2
        print(num)        
    
    elif num % 2 == 1:
        num = 3 * num + 1
        print(num)
        
print('Enter an integer:')

even_odd(num = int(input('>')))