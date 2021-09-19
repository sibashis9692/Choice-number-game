import random
random=random.randint(1,100)
usergess=None
gess=0
while(usergess!=random):
    usergess=int(input("enter your gess number: "))
    gess+=1
    if(usergess==random):
        print("Yes you gess the corect number")
    else:
        if(usergess>random):
            print("choose a small number")
        elif(usergess<random):
            print("choose a bigiest number")
print(f"your total gess number is {gess}")
with open("game.txt")as f:
    f.read()
with open("game.txt","w")as f:
    if("game.txt">str(gess)):
        f.write(str(gess))