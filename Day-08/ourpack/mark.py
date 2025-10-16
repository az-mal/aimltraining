class InvalidMarks(Exception):
    pass

def check_marks(marks):
    if (marks<0):
        print()
        raise InvalidMarks("Mark cannot be negative")
    elif (marks>50):
        print()
        raise InvalidMarks("Marks cannot be greater than 50")
    else:
        print(f"\nMark {marks} valid for assessement")