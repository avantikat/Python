# Health Management System
# 3 clients - avantika, parth and ved

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


#bhai ye rha program
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open(" avantika-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("avantika-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("parth-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("parth-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("ved-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("ved-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(avantika),2(parth),3(ved)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("avantika-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("avantika-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("parth-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("parth-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("ved-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("ved-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (avantika,parth,ved)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for avantika 2 for parth 3 for ved "))
    take(b)
else:
    b = int(input("Press 1 for avantika 2 for parth  3 for ved "))
    retrieve(b)

