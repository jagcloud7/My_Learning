#Print the multiplication of the number

print("Enter any number and I will show you its multiplication upto 10")

user_input_value = int(input('>'))

for num in range(1,11):
    multi_table = user_input_value * num
    print(f"{user_input_value} X {num} = {multi_table}")
    
print("Thank you!!! Dont forget to study the tables :)")