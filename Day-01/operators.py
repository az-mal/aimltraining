# Assignment operators: =, +=, -=
# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \n Discount: {discount} DiscountedPrice:{disPrice}")


# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus       #salary=salary+bonus
# print("Salary with Bonus",salary)


# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds         #salary=salary-tds
# print("Salary after tax",salary)


# if(condition)
#  #code
# else
#  #code


# age=int(input("Enter your age "))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("You are not eligible to cast your vote, you have to wait!")    
# print("End of program")


# marks=int(input("Enter marks percentage without '%' sign "))
# if(marks<30):
#     print("Failed")
# else:
#     print("Passed")
# print("Thank you!")


# accessCode="wes12"
# accessCode=input("Enter Access Code ")
# if(accessCode!="wes12"):
#     print("Invalid Access Code \nPlease try again" )
# else:
#     print("Permission granted \nThank you!")


# AccessCode="wes12"
# # accessCode=input("Enter Access Code ")
# count=0
# while count<3:
#     accessCode=input("Enter Access Code ")


#     if(accessCode=="wes12"):
#         print("Permission granted \nThank you")
#         break
#     else:
#         print("Invalid Access Code \nPlease try again")
#         count=count+1


#logical operators: and, or, not.
# phyMarks=int(input("Enter marks obtained in Physics "))
# chemMarks=int(input("Enter marks obtained in Chemistry "))
# mathsMarks=int(input("Enter marks obtained in Mathematics "))
# if((mathsMarks>=50) and (phyMarks>=55) and (chemMarks>=60)):
#     print("You are eligible to sit in the pre exam of MBBS")
# else:
#     print("You have not obtained the required marks to sit pre exam of MBBS")


# idProof=input("Enter Id proof yu have ")
# if((idProof=="passport")or(idProof=="license")or(idProof=="IC")):
#     print(f"Valid ID; we accept {idProof} here.")
# else:
#     print("Only passport, license and IC accepted as Identity Proof.")
#     print(f"{idProof} not valid as ID here.")


mathsMarks=int(input("Enter marks obtained in Mathematics "))
gapyear=int(input("Enter Year gap if any otherwise 0 "))
if((mathsMarks>=55) and (gapyear!=0)):
    print("Not eligible for BTech")
else:
    print("Eligible for BTech")
