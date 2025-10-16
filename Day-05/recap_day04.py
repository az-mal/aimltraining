def display():
    print("Welcome to recap of Function session")

def welcome(name):
    print("Welcome to Functions Mr./Ms.",name)

def cube(num):
    cube_num=num*num*num
    print(f"Cube of given number {num} is \t\t\t: \t{cube_num}")

def square(num):
    return num*num

def salBonus(salary):
    return salary*1.20

# *******************************

print('\n')

welcome("Mal") # <-- * the 2nd function above come out first because of the sequence arranged here *
display()
my_num=int(input("\nEnter a number to find out it's cubic result \t: \t  "))
cube(my_num)
# print(f"The square result of the number {num} is")
print('\n')
print(f"The square of {my_num} is \t\t\t\t: \t",square(my_num))

# * OR *
print('\n')
sqnum=square(my_num)
print(f"Square of {my_num} is \t\t\t\t\t: \t",square(my_num))

print('\n')
income=salBonus(my_num)
print(f"Income of {my_num} per hour should be t\t\t: \t",salBonus(my_num))

print('\n')
my_sal=float(input("Enter monthly salary to find out monthly bonus \t: \t"))
bonus=salBonus(my_sal)
print(f'\nSalary {my_sal} Bonus {bonus}')
print(f'\nSalary with bonus \t\t\t\t: \t',(my_sal+bonus))

print('\n')
