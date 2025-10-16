# import datetime
# import inspect

# print("Today is (Date): ",datetime.date.today())

# dtclasses=inspect.getmembers(datetime,inspect.isclass)
# print("All classes inside datetime module")

# for n, func in dtclasses:
#     print(n)

# print("All functions inside datetime.date class")

# functions=inspect.getmembers(datetime.date,inspect.isbuiltin)
# for n, func in functions:
#     print(n)

# # > same like below:
# numbers=[10,20,30,40,50]
# for n in numbers:
#     print(n)


import os

# listDirs=os.listdir()
# for dir in listDirs:
#     print(dir)

dirs=os.listdir()
for goat in dirs:
    print(goat)
