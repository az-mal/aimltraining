print('\n')

## class className:
    ## defination of class
        ## attribute Method, constructors

## objectName-ClassName()
## objectName.methodName()

##________________________________________________________________________________________________________________

# class Employee:
#     def display(intro):
#         print("Display of Employee Class")

# obj=Employee()
# obj.display()

# print('\n')
# e=Employee()
# e.display()

##________________________________________________________________________________________________________________

## another example
class Employee:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print("Employee Id \t:",self.eid)
        print("Employee name \t:",self.ename,"\n")

print("Employee details as follows")

e1=Employee()
e2=Employee()
e3=Employee()
e1.reg(1,'Sam')
e2.reg(102,'Neha')
e3.reg(103,'Jai')
print("\n")
print("First employee details")
e1.display()
print("Second employee details")
e2.display()
print("Third employee details")
e2.display()




#________________________________________________________________________________________________________________
print('\n')
        