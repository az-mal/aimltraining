from ourpack import calc

print()

#-------------------------------------------------------------------------------------------------

# * if using the elif-else, then the code will be like below:

# fnum=float(input("Enter first number \t\t:\t "))
# snum=float(input("Enter second number \t\t:\t "))
# print()
# op=input("Choose operation (+, -, *, /) \t:\t ")
# print()
# if(op=='+'):
#     print(f"Result: {calc.add(fnum,snum)} after adding {fnum} and {snum}")
# elif(op=='-'):
#     print(f"Result: {calc.sub(fnum,snum)} after subtracting {snum} from {fnum}")
# elif(op=='*'):
#     print(f"Result: {calc.multi(fnum,snum)} after multiplying {fnum} and {snum}")
# elif(op=='/'):
#     print(f"Result: {calc.div(fnum,snum)} after dividing {fnum} by {snum}")
# else:
#     print("Invalid Operation")

#-------------------------------------------------------------------------------------------------

# * if using the Try Except block, then the code will be like below:

# try:
#     fnum=float(input("Enter first number \t\t:\t "))
#     snum=float(input("Enter second number \t\t:\t "))
#     print()
#     op=input("Choose operation (+, -, *, /) \t:\t ")
#     print()
#     if(op=='+'):
#         print(f"Result: {calc.add(fnum,snum)} after adding {fnum} and {snum}")
#     elif(op=='-'):
#         print(f"Result: {calc.sub(fnum,snum)} after subtracting {snum} from {fnum}")
#     elif(op=='*'):
#         print(f"Result: {calc.multi(fnum,snum)} after multiplying {fnum} and {snum}")
#     elif(op=='/'):
#         print(f"Result: {calc.div(fnum,snum)} after dividing {fnum} by {snum}")
#     else:
#         print("Invalid Operation")
# except Exception as e:
#     print()
#     print("Error Occurred: ", e)
# finally:
#     print("Execution Completed")


#-------------------------------------------------------------------------------------------------

# * if using while loop, then the code will be like below:

fnum=float(input("Enter first number \t\t:\t "))
snum=float(input("Enter second number \t\t:\t "))
print()
while True:
    try: 
        op=input("Choose operation (+, -, *, /) \t:\t ")
        print("\n")
        if(op=='+'):
            print(f"Result: {calc.add(fnum,snum)} after adding {fnum} and {snum}")
        elif(op=='-'):
            print(f"Result: {calc.sub(fnum,snum)} after subtracting {snum} from {fnum}")
        elif(op=='*'):
            print(f"Result: {calc.multi(fnum,snum)} after multiplying {fnum} and {snum}")
        elif(op=='/'):
            print(f"Result: {calc.div(fnum,snum)} after dividing {fnum} by {snum}")
        else:
            print("Invalid Operation")
    except Exception as e:
        print()
        print("\nError Occurred: ", e)
    print()
    choice=input("\nDo you want to continue (y/n)? \t:\t ")
    if(choice.lower()!='y'):
            print("Bye")
            break



print()
#-------------------------------------------------------------------------------------------------