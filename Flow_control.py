# Real schools check:
# 1. Must pass each subject (minimum 35)
# 2. Grade based on total percentage

Name = input('Enter student name:\n>')
Maths = int(input('Enter total marks in Maths\n>'))
Science = int(input('Enter total marks in Science\n>'))
Languages = int(input('Enter total marks in Languages\n>'))

Total_marks = Maths + Science + Languages
Percentage = (Total_marks / 300) * 100

print(f'{Name} total marks is {Total_marks}')
print(f'Percentage: {Percentage:.1f}%')

# First check: Did student pass all subjects?
if Maths < 35 or Science < 35 or Languages < 35:
    print(f'{Name} has failed!')
    print('Reason: Failed in one or more subjects')
    if Maths < 35:
        print(f'  Maths: {Maths} - FAIL')
    if Science < 35:
        print(f'  Science: {Science} - FAIL')
    if Languages < 35:
        print(f'  Languages: {Languages} - FAIL')

# If passed all subjects - check grade
elif Percentage >= 90:
    print(f'{Name} has obtained Grade A+')
elif Percentage >= 80:
    print(f'{Name} has obtained Grade B+')
elif Percentage >= 70:
    print(f'{Name} has obtained Grade C+')
elif Percentage >= 40:
    print(f'{Name} has obtained Grade C')