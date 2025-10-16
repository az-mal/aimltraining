# * Take user marks from user within 0 to 50
# * If user enter number outside 0-50, then raise Error InvalidMarks using Custom Exception
# * Give chance to the user till he/she enter valid mark

#---------------------------------------------------------------------------------

print()

#---------------------------------------------------------------------------------
# * If using non-package module, then the code will be like below:

# class InvalidMarks(Exception):
#     pass

# def check_marks(marks):
#     if (marks<0):
#         print()
#         raise InvalidMarks("Mark cannot be negative")
#     elif (marks>50):
#         print()
#         raise InvalidMarks("Marks cannot be greater than 50")
#     else:
#         print(f"\nMark {marks} valid for assessement")

# while True:    
#     try:
#         usermarks=int(input("\nEnter your marks (0-50) \t:\t "))
#         check_marks(usermarks)
#     except InvalidMarks as e:
#         print("Invalid mark: ", e)
#     except Exception as ex:
#         print("Error Occurred: ", ex)
#     else:
#         print("Recorded Successfully \n")
#         break
#     print()
#     choice=input("To continue press y\nTo exit press any other key \t:\t")
#     if choice.lower()!='y':
#         print()
#         break

#---------------------------------------------------------------------------------

# * If using package module, then the code will be like below:

from ourpack import mark

while True:
    try:
        usermarks=int(input("\nEnter your marks (0-50) \t:\t "))
        mark.check_marks(usermarks)
    except mark.InvalidMarks as e:
        print("Invalid mark: ", e)
    except Exception as ex:
        print("Error Occurred: ", ex)
    else:
        print("Recorded Successfully \n")
        break
    print()
    choice=input("To continue press y\nTo exit press any other key \t:\t")
    if choice.lower()!='y':
        print()
        break

#---------------------------------------------------------------------------------
print()


    