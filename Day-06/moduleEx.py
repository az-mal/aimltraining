#_______________________________________________________________________________________
print('\n')
#_______________________________________________________________________________________

# import math
# my_num=int(input("Enter number to find out the square root : \t"))
# print(f"Square root of {my_num} is: {math.sqrt(my_num):.2f}") # <--- math is already a module in library


#_______________________________________________________________________________________

# * print your lucky number form 1 to 100 is: random.randint(1,100)

# * to check function inside module
import math
import inspect

functions = inspect.getmembers(math, inspect.isbuiltin)
# print(functions)

# > to see all built-in functions under Maths module: 
# for n, func in functions:
#     print(n)

# > example:
print("\nsin 90 is : \t",math.sin(90))
print("cos 90 is : \t",math.cos(90))
print("tan 90 is : \t",math.tan(90))

deg=int(input("\nDegree to find out cos "))
print(f"\ncos(deg) is: ",math.cos(deg))

#_______________________________________________________________________________________
print('\n')
#_______________________________________________________________________________________