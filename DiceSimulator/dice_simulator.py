import random

print("This is Dice")
x=''
while x=='':
    number=random.randint(1,6)
    if number==1:
            print("_________")
            print("|       |")
            print("|   0   |")
            print("|       |")
            print("_________")
    if number==2:
            print("_________")
            print("|       |")
            print("|  0  0 |")
            print("|       |")
            print("_________")
    if number==3:
            print("_________")
            print("|       |")
            print("| 0 0 0 |")
            print("|       |")
            print("_________")
    if number==4:
            print("_________")
            print("|  0  0 |")
            print("|       |")
            print("|  0  0 |")
            print("_________")
    if number==5:
            print("_________")
            print("|  0  0 |")
            print("|   0   |")
            print("|  0  0 |")
            print("_________")
    if number==6:
            print("_________")
            print("|  0  0 |")
            print("|  0  0 |")
            print("|  0  0 |")
            print("_________")
    x=input("press enter to roll again")
            
