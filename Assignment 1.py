# Python-Prateek-Sir
#program to add three numbers
print('Program 1')
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

print(f'Sum = {num1+num2+num3}')

#program to display name and roll no.
print('Program 2')

name = input("Enter your name: ")
roll_no = int(input("Enter your Roll No. : "))

print(f'Name : {name}')
print(f'Roll No. : {roll_no}')

#program to concatenate two strings
print('Program 3')

first_name = input("Enter First Name : ")
last_name = input("Enter Last Name : ")

#concatenating two strings and assigning it to a new string
full_name = first_name + " " + last_name

print(f'Name : {full_name}')

#program to declare and assigning values to multiple variables in a single line
print('Program 4')
x,y,z = 33,17.5,"Python"

print(type(x))
print(type(y))
print(type(z))

#program to convert the type of the variable
print('Program 5')

x = 17
print(f'Type of x is {type(x)}')

#type casting
y = complex(x,0)
print(f'{type(y)}')

