import random
print("Instructions\n 0 is for Rock \n 1 is for Paper \n 2 is for scissors")

ai=random.randint(0,2)
if ai==0:
    print("rock")
if ai==1:
    print("paper")
if ai==2:
    print("scissors")

choose = int(input("choose between 0 , 1 , 2 : "))
if choose==0:
    print("rock")
if choose==1:
    print("paper")
if choose==2:
    print("scissors")

if ai==0:
    if ai==0 and choose==0:
        print("clash")
    if ai==0 and choose==1:
        print("WIN")
    if ai==0 and choose==2:
        print("LOOSE")
if ai==1:
    if ai==1 and choose==0:
        print("LOOSE")
    if ai==1 and choose==1:
        print("clash")
    if ai==1 and choose==2:
        print("WIN")
if ai==2:
    if ai==2 and choose==0:
        print("WIN")
    if ai==2 and choose==1:
        print("LOOSE")
    if ai==2 and choose==2:
        print("clash")
