print('\n')
#__________________________

class Emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual


    def display(self):
        print('ID: ',self.id)
        print('Name: ',self.name)
        print("Quali: ",self.qual)
    
class Dev(Emp):
    def __init__(self,id,name,qual,domain,project):
        super().__init__(id,name,qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print("Domain: ",self.domain)
        print("Project: ",self.project)


# * Exercise below : *

# * 1. Create 1 Emp object with id=1, name='Sam', qual='MCA'
emp=Emp(1,'Sam','MCA')

# * 2. Create 1 Dev object with id=2, name='Ravi, Qual='MTech', Project='eShopping', Domain='dot net'
dev=Dev(3,'Ravi','MTech','eShopping','dot net')

# * 3. Display Dev details
print("\nDeveloper details as follows: ")
dev.display()

# * 4. Display Emp details
print("\nEmployee details as follows: ")
emp.display()


#__________________________
print('\n')

