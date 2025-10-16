# numbers = [10,25,30,40,2,1]
# double_num=list(map(lambda x: 2*x, numbers))
# print('Original List')
# for num in numbers:
#     print(num,end=" ")

# print('\n\nDouble List')
# for num in double_num:
#     print(num,end=" ")

# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print('\nEven numbers from list as follows\n')
# for num in even_numbers:
#     print(num,end=" ")

# odd_numbers=list(filter(lambda x:x%2==1,numbers))
# print('\Odd numbers from list as follows\n')
# for num in odd_numbers:
#     print(num,end=" ")

#_________________________________________________________________________________________
print("__________TASK FOR MAP FUNCTION__________")
print("Question: Write code using filter to find out all the number less than 5")

our_list=[4,2,5,6,7,3,1,10]
num_less5=list(filter(lambda x:x<5,our_list))

print(f'\nThe list are {our_list}')
print('The numbers that is less than 5 from list is as follows:',num_less5)
# for num in num_less5:
#     print(num,end=" ")
#_________________________________________________________________________________________