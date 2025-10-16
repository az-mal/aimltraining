print()

class InvalidAge(Exception):
    pass
def check_age(age):
    if age<0:
        raise InvalidAge("Age cannot be negative")
    elif age<18:
        raise InvalidAge("Underage: Not eligible for employment")
    elif age>=80:
        raise InvalidAge("Too old for employment")
    else:
        print(f"Age {age} is accepted and valid for employment")

try:
    userage=int(input("Enter your age \t:\t "))
    check_age(userage)
except InvalidAge as e:
    print("Invalid Age: ", e)
except Exception as ex:
    print("Error Occurred: ", ex)


#-------------------------------------------------------------------------------------------------

print()
