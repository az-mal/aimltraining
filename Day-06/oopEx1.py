print('\n')

#_____________________________________________________________________________________________________________________________________

# class Player:
#     def __init__(self):
#         print("Welcome to Player Class")

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team
    
#     def display(self):
#         print(f"Id:{self.id} \t Name: {self.name} \t Team: {self.team} ")


# * OBJECT CREATION *
# p1=Player()
# p2=Player()
# p3=Player()
# p1.reg(1,'MSD','India')
# p2.reg(2,'R.Khan','Afghanistan')
# p3.reg(3,'Moin Ali','England')

# p1.display()
# p2.display()
# p3.display()

#______________________________________________________________________________________________________________________________________________________________________________

class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team
    
    def display(self):
        print(f"Id:{self.id} \t Name: {self.name} \t Team: {self.team} ")

    def __str__(self):
        return f'{self.id} {self.name} {self.team}'

p1=Player(1,'MSD','India')
p2=Player(2,'Moin Ali','England')
p3=Player(3,'Joe Root','England')

#___________________________________________________________________________________________________________________________________________________________________________________________

# * displayng player details *
# * this goes along with normal display (without string) method *
# p1.display()
# p2.display()
# p3.display()

#______________________________________________________________________________________________________________________________________________________________________________________

# * this goes along woth the __str__ string function *
print(p1)
print(p2)
print(p3)

#_____________________________________________________________________________________________________________________________________________________________________________________________

print('\n')
