# * default parameter in function *
# print('\n')
# print("Details as follows \t: \n")
# def info(id,name,city='KL'):
#     print(f"ID: {id} \tName: {name} \tCity: {city}")

# info(1,'Sam','New Delhi')
# info(101,'Xi')
# info(103,'Chang')
# print('\n')


# * if we would want to create a single method that able to add certain numbers and return correct total *
# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5

# print("Result \t:",add(1,2))
# print("Result \t:",add(5,3,1,4,10))
# print("Result \t:",add(5,25,10))


# def add(*args):
#     return sum(args)
# print('\n')
# print('Sum of 1,10,11 is: \t',add(1,10,11))
# print('Sum of 5,2 is: \t',add(5,2))
# print('Sum of 10,10,100,100,200,219,19 is: \t',add(10,10,100,100,200,219,19))
# print('\n')
# print('Maximum of 1,10,11 is: \t',max(1,10,11))
# print('Maximum of 5,2 is: \t',max(5,2))
# print('Maximum of 10,10,100,100,200,219,19 is: \t',max(10,10,100,100,200,219,19))
# print('\n')
# print('Minimum of 1,10,11 is: \t',min(1,10,11))
# print('Minimum of 5,2 is: \t',min(5,2))
# print('Minimum of 10,10,100,100,200,219,19 is: \t',min(10,10,100,100,200,219,19))
# print('\n')


# *write a python function which converts inches to cms. *
# * 1 inch = 2.5 cm *
# print('\n')
# def inch_to_cm(num):
#     return num*2.5

# num=int(input("Enter a measurement in inch to be converted to cm \t:\t"))
# print(f"{num} in inch equal to \t\t\t\t\t: \t{inch_to_cm(num)} cm")
# print('\n')


# * write a function to display username *
def display(username):
    print(f"{username}")
username=int(input("Enter username \t:\t"))



# * write a function to find out the table of given number *
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input("Enter number to find out table "))
gen_table(number)


  
