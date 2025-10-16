# *** LAMBDA *** another method for defining calculations

# * below is convential way *
# def add(a,b):
#     total=a+b
#     print(f"{total}")

# print("\n")
# result=add(12,15)
# print(result)

# * below if we want to use lambda method instead *

add=lambda a,b:a+b
sub=lambda a,b:a-b
multi=lambda a,b:a*b
div=lambda a,b:a/b
avg=lambda a,b:(a+b)/2

print("\n")

print(add(12,15))
print("\n")
num1=int(input("Enter a number \t\t:\t"))
num2=int(input("Enter another number \t:\t"))

print("\nThe average result for the numbers are \t:\t",avg(num1,num2))
print("\nThe dvision result for the numbers are \t:\t",div(num1,num2))

print("\n")