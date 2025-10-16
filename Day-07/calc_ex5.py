print("\n")
#________________________________________________________________________________________

import calc # <--- this module created by us in the calc.py file in the same folder *
import ex2
first_num=float(input("Enter first number \t:\t"))
second_num=float(input("Enter second number \t:\t"))

print(f"\nTotal of {first_num} and {second_num} \t=\t{calc.add(first_num, second_num):.2f}")
ex2.findwinner()

#________________________________________________________________________________________
print("\n")
