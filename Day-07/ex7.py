# # * use when you want to handle any kind of exception
# # * use when you want to execute some code no matter if exception occurs or not
# # * use when you want to avoid program crash due to exception
# # * use when you want to display custom error message

#--------------------------------------------------------------------------------

# print()

# try:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     total=num1+num2
#     print(f"\nTotal of {num1} and {num2} is {total}\n")
# except Exception as e:
#     print(f"\nError: {e}\n")
#     print("End of program due to error.\n")
# finally:
#     print("End of program.\n")

#--------------------------------------------------------------------------------

print()

try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    div=num1/num2
    print(f"\nResult after dividing {num1} by {num2} = {div}\n")
except Exception as e:
    print(f"\nError: {e}\n")
    print("End of program due to error.\n")
finally:
    print("End of program.\n")

print()
#--------------------------------------------------------------------------------
