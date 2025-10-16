print('\n')
#_____________________________________________________________________________________________________________________________________

# class Bird:
#     def fly(self):
#         print("Bird can fly")

# class Airplane(Bird):
#     def fly(self):
#         print("Airplane fly")

# b=Bird()
# print("Bird Implement")
# b.fly()

# print("\nAirplane Implementation")
# a=Airplane()
# a.fly()
# print("\nUsing for loop:")
# for obj in [Bird(), Airplane()]:
#     obj.fly()

#_____________________________________________________________________________________________________________________________________

class Emp:
    def reg(self):
        self.id=int(input("Enter Id: "))
        self.name=input("Enter Name: ")

    def disp(self):
        print("Name",self.name)
        print("ID",self.id)
    
d1=Emp()
d1.reg()
d1.disp()

print('\n')
class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input("Enter Domain: ")

    def disp(self):
        super().disp()
        print("Domain: ",self.domain)


d1=Dev()
d1.reg()
d1.disp()

#_____________________________________________________________________________________________________________________________________
print('\n')
