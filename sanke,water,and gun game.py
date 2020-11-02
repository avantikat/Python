import random
list = [ "snake","water","gun"]
choice = random.choice(list)
def won():
    if i == 1:
        print("You won the ", i, "st game")
    elif i == 2:
        print("You won the ", i, "nd game")
    elif i == 3:
        print("You won the ", i, "rd game")
    else:
        print("You won the ", i, "th game")
    return i+1

def loose():
    if i == 1:
        print("You loose the ", i, "st game")
    elif i == 2:
        print("You loose the ", i, "nd game")
    elif i == 3:
        print("You loose the ", i, "rd game")
    else:
        print("You loose the ", i, "th game")
    return i+1

def tie():
    if i == 1:
        print("You tie the ", i, "st game")
    elif i == 2:
        print("You tie the ", i, "nd game")
    elif i == 3:
        print("You tie the ", i, "rd game")
    else:
        print("You tie the ", i, "th game")
    return i+1
A = 0
B = 0



print("we play one game whose name is snake,water,and gun:\n you have 9 chances")
i=1
while i<10:
    print("press:\n s for sanke\n w for water\n g for gun:")
    a=input()
    if a=="s":
      if choice=="snake":
        print(" you tie the game with the computer")
        print(tie())
        a=1
        i=i+1
      elif choice=="water":
        print("you won the game with the computer as snake drunk the water")
        print(won())
        a=2
        i=i+1
      else:
        print("you loose the game with the computer as gun kill the sanke")
        print(loose())
        a=3
        i=i+1
    elif a=="w":
      if  choice=="water":
        print(" you tie the game with the computer")
        print(tie())
        a=1
        i=i+1
      elif choice=="gun":
       print("you won the game with the computer as the gun  sanke in water ")
       print(won())
       a=2
       i=i+1
      else:
       print("you loose the game with the computer as snake drunk the water")
       print(loose())
       a=3
       i=i+1
    elif a=="g":
     if choice=="gun":
       print(" you tie the game with the computer")
       print(tie())
       a=1
       i=i+1
     elif choice=="sanke":
       print("you loose the game with the computer as snake has beem killed with gun")
       print(won())
       a=2
       i=i+1
     else:
       print("you loose the game with the computer as gun sunk in the water")
       print(loose())
       a=3
       i=i+1
    else:
       print("you entered wrong choice plz enter a right choice")
    continue
if a==2:
     A=A+1
elif a==3:
     B=B+1
if A>B:
    print("You won the game by winning ",A," times")
else:
    print("You loose the game by loosing ",B," times")
