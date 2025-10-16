# *** TUPLE ***

# print("We are going to discuss about TUPLE here")
# subjects=("python","java","dotnet","sql","power bi")
# print("\n All subjects : \n")
# print("Number of subjects are : ",len(subjects))
# for sub in subjects:
#     print(sub,end=", ")


# * Example 1 *

# * use tupleName.index(item) to show index of first occurence item in the tuple : *
# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print("\nTotal number in tuple :",len(numbers))
# # print(numbers)
# for num in numbers:
#     print(num,end=", ")
# search_num=int(input("\n\nEnter which index from list for the number of :\t"))
# if search_num in numbers:
#     print(f"Index of {search_num} is : \t ",numbers.index(search_num))
# else:
#     print("\n")
#     print("Sorry, no such number {search_num} of index in the tuple.")


# # * to check base on frequency : *
# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print("\nTotal number in tuple :",len(numbers))
# # print(numbers)
# for num in numbers:
#     print(num,end=", ")
# search_num=int(input("\n\nEnter any number to find out the frequency :\t"))
# if search_num in numbers:
#     print(f"\nNumber \t\t: \t{search_num} \nOccuring \t: \t{numbers.count(search_num)} times\n")
# else:
#     print("\n")
#     print("Sorry, no such number {search_num} in the tuple\n")


# * Exercise *
# * Write a program to sum a list with 4 numbers. *
# * since exercise asks for list then to use round bracket () instead of square bracket [] which is for tuple *
# numbers=[4,10,50,7]
# print("\nTotal number in tuple :",len(numbers))
# total=sum(numbers)
# print("\n\nSum of the numbers is : ",total)