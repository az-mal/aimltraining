def add(num1,num2):
    return num1+num2
def multi(num1,num2):
    return num1*num2
def avg(num1,num2):
    return (num1+num2)/2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
print('\nWelcome to our Calculator\n')
fnum=float(input('Enter first number \t:\t'))
snum=float(input('Enter second number \t:\t'))
while True:
    print('\nSelect operation : \n1.Add \n2.Sub \n3.Multiply \n4.Division \n5.Average \n6.Exit\n')
    op=int(input('\nEnter selection number (1-6) \t:\t'))
    print('\n')
    if(op==6):
        print('Thank you and goodbye')
        break
    if((op>=6)or(op<=0)):
        print('Selection cannot be defined. Please choose again')
        break
    print('\n`')
    if(op==1):
        print(f'Result adding of {fnum} , {snum} : \t',add(fnum,snum))
    elif(op==2):
        print(f'Result subtracting of {fnum} , {snum} : \t',sub(fnum,snum))
    elif(op==3):
        print(f'Result multiplying of {fnum} , {snum} : \t',multi(fnum,snum))
    elif(op==4):
        print(f'Result dividing of {fnum} , {snum} : \t',div(fnum,snum))
    elif(op==5):
        print(f'Result averaging of {fnum} , {snum} : \t',avg(fnum,snum))
        


