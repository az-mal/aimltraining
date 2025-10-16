print()
#-------------------------------------------------------------------------------------------------

try:
    fnum=float(input("Enter first number \t:\t "))
    snum=float(input("Enter second number \t:\t "))
    result=fnum/snum
    print()
    print(f"Result: {round(result,4)} after dividing {fnum} by {snum}") #<--- decimal rounding using round() function
    #  or 
    print(f"Result: {result:.4f} after dividing {fnum} by {snum}") #<--- decimal rounding using f-string formatting
except Exception as e:
    print()
    print("Error Occurred: ", e)
finally:
    print("Execution Completed")









#-------------------------------------------------------------------------------------------------
print()
