import os

#---------------------------------------------------------------------------------

# file_path = "/Volumes/SToR/1 MINE/STuDieS/YP/AIML/Day-08/ourfiles/sample.txt"
# with open(file_path, "w") as file:
#     file.write("Hello, this is a test!")

# <-- if want to command current opened active file, just type below: 
# filepath=os.getcwd()

#---------------------------------------------------------------------------------

# filepath="/Volumes/SToR/1 MINE/STuDieS/YP/AIML/Day-08/ourfiles"
# filename=input("Enter file name to create: \t:\t")
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,"w")
# content=input("Enter content to write in file: \t:\t")
# file.write(content)
# print(f"File '{filename}' created at '{filepath}' and content saved in file")
# file.close()

#---------------------------------------------------------------------------------

# <--- to add content to existing file without checking if file exists or not

# filepath="/Volumes/SToR/1 MINE/STuDieS/YP/AIML/Day-08/ourfiles"
# filename=input("Enter file name to update file: \t:\t")
# fullpath=os.path.join(filepath,filename)

# file=open(fullpath,"a")

# content=input("Enter text to add: \t:\t")
# file.write(content)
# print(f"File '{filename}' updated")
# file.close()

#---------------------------------------------------------------------------------

# <--- to add content to existing file only if file exists, else show message that file does not exist

# filepath="/Volumes/SToR/1 MINE/STuDieS/YP/AIML/Day-08/ourfiles"
# filename=input("\nEnter file name to update file: \t:\t")
# fullpath=os.path.join(filepath,filename)

# if(os.path.exists(fullpath)):
#     file=open(fullpath,"a")
#     content=input("Enter text to add: \t:\t")
#     file.write(content)
#     print(f"File '{filename}' updated")
#     file.close()
# else:
#     print(f"\nFile '{filename}' does not exist in '{filepath}'")
# print()

#---------------------------------------------------------------------------------



filepath="/Volumes/SToR/1 MINE/STuDieS/YP/AIML/Day-08/ourfiles"
filename=input("\nEnter file name to update file: \t:\t")
fullpath=os.path.join(filepath,filename)

if(os.path.exists(fullpath)):
    file=open(fullpath,"r")
    content=file.read()
    print(f"\nFile content as follows")
    print()
    print(content)
    file.close()
else:
    print(f"\nNo such {filename}' exist")
print()