employee={"Id":1,
"Name":"Sam",
"Salary":55000.50
}
print("\n")
print("Employees Details as follows:")
for key,value in employee.items():
    print(key,"\t\t",value)

employee["City"]="Muscat"
print('\nDictionary after adding City\n')
for key,value in employee.items():
    print(key,"\t\t",value)
print("\n")

del employee["Salary"]
print('\nEmployee details after deleting salary \n')
for key,value in employee.items():
    print(key,"\t\t",value)
print("\n")

print("\nall Keys from employee\n")
for v in employee.keys():
    print(v,end="\n")
print("\n")

print("\nall Values from employee\n")
for v in employee.values():
    print(v,end="\n")

print('\nKey:Value')
for k,v in employee.items():
    print(k,"\t :",v)

print('\nDictionary as follows')
print(employee)
print("\n")