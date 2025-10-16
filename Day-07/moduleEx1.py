print("\n")
#________________________________________________________________________________________


# import math
# num=int(input("Enter number to find out square root \t: "))
# print(f"Square root of {num} \t{math.sqrt(num):.2f}")
# print(f"Square root of {num} \t",round(math.sqrt(num),2))


#________________________________________________________________________________________

# import math
# import inspect

# functions=inspect.getmembers(math, inspect.isbuiltin)

# print("All functions in math module")
# for n, func in functions:
#     print(n,end="\t")


#________________________________________________________________________________________


# import datetime
# import inspect

# dtclasses=inspect.getmembers(datetime, inspect.isclass)

# print("All classes in datetime module\n")
# for n, func in dtclasses:
#     # print(n,end="\t")
#     print("◉",n)

# print("\n --- Calling ---\n")
# print(datetime.date.today())

# print("\n ---Current Date Time ---\n")
# print(datetime.datetime.now())

# print("\n ---Current Time ---\n")
# print(datetime.datetime.now().time())

# cttime=datetime.datetime.now().time()
# formattedtime=datetime.datetime.now().strftime("%I: %M: %S: %p")
# print("Current time",cttime)
# print("Formatted time",formattedtime)


#________________________________________________________________________________________


# import random
# print("Random number from 1 to 1000\n")
# print(random.randint(1,1000))


#________________________________________________________________________________________

# * Random Lucky Number *

# import random
# name=input("Enter your name \t:\t")
# luckyNumber=random.randint(1,10)
# if(luckyNumber==1):
#     print(f"", name, "You have won a Proton X50!")
# elif(luckyNumber==3):
#     print(f"", name, "You have won a Proton X70!")
# elif(luckyNumber==9):
#     print(f"", name, "You have won a Proton X90!")
# else:
#     print("Better luck next time! ⎛⎝ ≽ > ⩊ < ≼ ⎠⎞")
    

#________________________________________________________________________________________


# # * To check all functions available in the python *
# import os
# import inspect
# print("Current directory: ",os.getcwd())
# print("Login name:",os.getlogin())

# functions=inspect.getmembers(os,inspect.isbuiltin)

# print("All function in os module")
# for n, func in functions:
#     print(n)


#________________________________________________________________________________________


# # * To create a folder insude current directory using python *

# import os
# cdir=os.getcwd()
# folder_name=input("Enter folder name to create \t:\t")
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print("Folder already exists")
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f"{folder_name} created at {folder_path}")


#________________________________________________________________________________________


# # *  To rename folder *

import os
cdir=os.getcwd()
old_folder_name=input("Enter the existing folder to rename \t:\t")
if(os.path.exists(old_folder_name)):
    new_folder_name=input("Enter new folder name \t:\t")
    os.rename(old_folder_name,new_folder_name)
    print(f"folder renamed as: ",{new_folder_name})
else:
    print("Folder does not exists")





#________________________________________________________________________________________


# *  To delete folder *

#________________________________________________________________________________________






#________________________________________________________________________________________
print("\n")