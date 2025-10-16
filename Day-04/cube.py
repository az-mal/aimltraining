# print('\n\nLet's find the cube of a number')

# def cube(num1):
#     return num1*num1*num1
# fnum=float(input('\n\nEnter any number \t\t:\t '))
# print(f'\nResult for the cube of {fnum} \t:\t',cube(fnum))
# print('\n')

# write a function to calculate the bonus of given salary
# function take salary as input and return bonus (10% of salary)

print("\n\nLet's find out how much your earning\n")

def earning(salary,bonus):
    return salary+(salary*(bonus/100))
salary=float(input('\n\nEnter your salary \t\t\t\t\t\t\t:\t '))
bonus=float(input('\nEnter your bonus % \t\t\t\t\t\t\t:\t '))
print(f'\nYour expecting bonus should be RM{salary:.2f} with a bonus of {bonus}% \t:\tRM',earning(salary,bonus))
print('\n')