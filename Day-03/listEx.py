# *** LIST ***
# it is done by using square bracket[]

# print('List Example One')

# my_list = [10, 20, 30, "Python",None,True,12.45]


# * for item in my_list: *
# *    print(item) *

# * print('List Example One') *
# my_list = [10, 20, 30, "Python",None,True,12.45,'Ravi']
# print('Number of items in list are:',len(my_list))

# for item in my_list:
#     print(item)


# print not in list, but in just a row as whats being originally written:
# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees",len(emps))
# print("All Employees")
# print(emps)


# print not in list, but in just a row with spaces between items:
# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees",len(emps))
# print("All Employees")
# for emp in emps:
#     print(emp,end=" ")


# print as list:
# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees",len(emps))
# print("All Employees")
# for emp in emps:
#     print(emp)



# *** SORT ***

# * Ascending order *
# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees",len(emps))
# print("All Employees")
# emps.sort()
# print("List after sorting")
# for e in emps:
#     print(e,end=" ")


# * Descending order *
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# emps.sort()
# emps.reverse()
# print("\n in descending order")
# for e in emps:
#     print(e,end=" ")
    


# *** APPEND, REMOVE, POP INSERT METHOD ***

# ** 1. APPEND **
# * adds the item at the end of the list *
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for e in emps:
#     print(e,end=" ")
# newEmp=input("\nenter employee name to add to the list :\t")
# emps.append(newEmp)
# print("The list after adding new employee: Number of employees are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")


# ** 2. INSERT **
# * adds the item anywhere in the list *
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for e in emps:
#     print(e,end=" ")
# newEmp=input("\nEnter employee name to add in the list:\t")
# pos=int(input("Enter the position where you want to insert to the list:\t"))
# emps.insert(pos-1,newEmp)
# print("\nAfter adding New Employee: Number of employees are :",len(emps))
# for emp in emps:
#     print(emp,end=" ")


# ** 3. REMOVE **
# * remove item from a list use delList or delete_list command *
# * listName.remove(item): Will remove item
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for e in emps:
#     print(e,end=" ")
# delEmp=input("\nName to be removed :\t")
# emps.remove(delEmp)
# print(f"Number of employees after deleting {delEmp} in list are:",len(emps))
# for e in emps:
#     print(e,end=" ")


# * if want to add checker for removing item whether in the list *
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for e in emps:
#     print(e,end=" ")
# delEmp=input("\nName to be removed :\t")
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employees after deleting {delEmp} in list are:",len(emps))
#     for e in emps:
#         print(e,end=" ")
# else:
#     print(f"No such item {delEmp} is in the list")


# ** 4. POP ***
# * to remove based on entry number in list *
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for e in emps:
#     print(e,end=" ")
# del_index=int(input("\nEnter index to pop item :\t"))
# print('Pop result: ',emps.pop(del_index-1)) # add -1 to command according to end user understanding
# print(f"Number of employees after pop out are:",len(emps))
# for e in emps:
#     print(e,end=" ")


# * Exercise *
# * Write a program to sum a list with 4 numbers. *
numbers=[4,10,50,7]
print("\nTotal number in tuple :",len(numbers))
total=sum(numbers)
print("\n\nSum of the numbers is : ",total)