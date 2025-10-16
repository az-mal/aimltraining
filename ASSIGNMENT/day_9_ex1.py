print()

def greatest_number(max):
    return max
num1=int(input("Enter first number \t: "))
num2=int(input("Enter second number \t: "))
num3=int(input("Enter third number\t: "))
max=num1
if num2>max:
    max=num2
if num3>max:
    max=num3
print()
print("Greatest number is \t:",greatest_number(max))

print()