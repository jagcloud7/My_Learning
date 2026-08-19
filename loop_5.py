# Printing numbers range

import sys

i = 1
j = 1
k = 10

print('Part A:')
for i in range(1,11):
    print(f'Printing numbers {int(i)}')
    i = i + 1

print('Part B:')
for j in range(2,21,2):
    print(f'Printing even numbers only {int(j)}')
    j = j + 1

print('Part C:')
for k in range(10,0,-1):
    print(f'Countdown begins: {int(k)}')
    k = k - 1
    
sys.exit()