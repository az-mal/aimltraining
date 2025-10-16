print('\n')

# numbers = [10, 25, 30, 40, 2, 1]

# print("Original List")
# for num in numbers:
#     print(num, end=" ")

# even_numbers=list(filter(lambda x: x%2==0, numbers))

# print('\n')

# print("Even numbers from list as follows")
# for num in even_numbers:
#     print(num, end=" ")



# * you have following list *
our_list= [4,2,5,6,7,3,1,10]
# * write code using filter to find out all the numbers more than 5 from the list *

# print("Original List")
# for num in our_list:
#     print(num, end=" ")

# numbers_bigger5=list(filter(lambda x: x>5, our_list))

# print('\n')

# print("Numbers bigger than 5 from list as follows")
# for num in numbers_bigger5:
#     print(num, end=" ")



students_marks={'Sam':60,
                'Raj':55,
                'Mihir':35,
                'Sandy':45,
                'Niraj':76,
                'Deep':40,
                'Garima':54
                }
print('All Students \t\t:')
print(students_marks)

print('\n')
pass_students=dict(filter(lambda i:i[1]>=50, students_marks.items())) # <--- [1] refer to the 2nd entry (score) in lambda sequence name,score
print("Passed students \t:")
print(pass_students)

print('\n')
fail_students=dict(filter(lambda i:i[1]<=50, students_marks.items()))
print("Failed students \t:")
print(fail_students)

print("\n")
for k,v in students_marks.items():
    print(f'{v} - Name : {k}')

sort_students_marks_desc=dict(sorted(students_marks.items(), key=lambda x: x[1],reverse=True))

print('\n')
print("Based on marks in descending order")
for k,v in sort_students_marks_desc.items():
    print(f'{v} : {k}')
print('\n')

sort_students_marks=sorted(students_marks.items(), key=lambda x: x[1])
print(sort_students_marks)

print('\n')
sort_students_marks_desc=sorted(students_marks.items(), key=lambda x: x[1],reverse=True)
print(sort_students_marks_desc)

print('\n')