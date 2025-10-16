print('\n')

#_____________________________________________________________________________________________________________________________________

class Empl:
    def welcome(self):
        print('Welcome ExxonMobil Staff')

    def reg(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print("Id: ",self.id)
        print("Name: ",self.name)

class Dev(Empl):
    def welcome(self):
        print('Welcome Marketing Staff')

e=Empl()
e.welcome()
e.reg(102, "Raj")
e.display()

print('\n')
d=Dev()
d.welcome()
d.reg(1,"Sam")
d.display()




#_____________________________________________________________________________________________________________________________________

print('\n')