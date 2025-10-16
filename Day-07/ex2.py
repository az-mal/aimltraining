import random
def findwinner():
    name=input("Enter your name \t:\t")
    luckyNumber=random.randint(1,10)
    print(f"Welcome Mr.\\Ms {name} Coupon Number: {luckyNumber}")
    if(luckyNumber==1):
        print(f"", name, "You have won a Proton X50!")
    elif(luckyNumber==3):
        print(f"", name, "You have won a Proton X70!")
    elif(luckyNumber==9):
        print(f"", name, "You have won a Proton X90!")
    else:
        print("Better luck next time! ⎛⎝ ≽ > ⩊ < ≼ ⎠⎞")