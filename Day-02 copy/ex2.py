# use WHILE loop to make looping with unexpected condition e.g. now knowing how many times.
# in the case we already know the number of loop, can use FOR loop.

# num=1
# print('Printing Numbers from 1 to 100')
# while(num<=100):
#     print(num,end=" ")
#     num+=1


# BREAK example

# num=1
# print('Printing Numbers from 1 to 100 before we get to the number divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         break
#     print(num,end=" ")
#     num+=1


# CONTINUE example

# notice the numbers that can be divided by 11 won't appear
# num=1
# print('Printing Numbers from 1 to 100 those are not divisible by 11')
# while(num<=100):
#     if(num%11==0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1


# opposite : notice the numbers that can be divided by 2 appear because change == to !=
# print('Oddnumnbers from 1 to 100')
# num=1
# while(num<=100):
#     if(num%2!=0):
#         num+=1
#         continue
#     print(num,end="\t")
#     num+=1


# or can use 'for' method to loop as example below:
# for i in range(1,100):
#     if (i%5!=0):
#         continue
#     print(i,end="\t")


# loop example using while for password attempts
# correctPwd='sam@1256'
# while True:
#     pwd=input('Enter password to start : \t')
#     if(correctPwd==pwd):
#         print('Welcome! Access granted.')
#         print('*** Starting Mission ***')
#         break
#     else:
#         print('Wrong password. Please try again.')


#if only want to give 3 attempts
correctPwd='sam@1256'
counter=1
while True:
    pwd=input('Enter password to start : \t')
    if(correctPwd==pwd):
        print('Welcome! Access granted.')
        print('*** Starting Mission ***')
        break
    else:
        print('Wrong password. Please try again.')
        counter+=1
        if(counter>3):
            print('Too many attempts. Please contact admin')
            break


    
