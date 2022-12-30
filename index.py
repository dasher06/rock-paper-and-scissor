import random
from getpass import getpass
a=input("Enter your name ")
print("Bot: Hi",a,"!")
print("Bot: Ready to play rock ,paper and scissors !")
print("Bot: There are two modes")
print("Bot: Bot vs Player(1st) and Player1 vs Player2(2nd)")
print("Bot: To play 1st mode enter (c)and to play second mode enter any string(letters)")
b=input(a+": ")
if b=="C" or b=="c":
    l=["rock","paper","scissor","Rock","Paper","Scissor"]
    print("Bot: I have entered ,it's your turn")
    p1=random.choice(l)
    p2=input(a+": ")
    p3=p2.lower()
    if (p1==p3):
        print("Game tied")
    else:
        if p1=="rock":
            if p3=="paper":
                print(a,"is the winner!!")
            if p3=="scissor":
                print("Bot is the winner!1")
        else:
            if p1=="paper":
                if p3=="rock":
                    print("Bot is the winner!!")
                if p3=="scissor":
                    print(a,"is the winner!!")
            else:
                if p1=="scissor":
                    if p3=="paper":
                        print("Bot is the winner!!")
                    if p3=="rock":
                        print(a,"is the winner")
                else:
                    print("Wrong input")
else:
    c=input("Bot: Enter second player name ")
    print("Bot: Now the game is between",a,"and",c,"!!")
    p3=getpass(a+": ")
    p5=p3.lower()
    p4=input(c+": ")
    p6=p4.lower()
    if (p5==p6):
        print("Game tied")
    else:
        if p5=="rock":
            if p6=="paper":
                print(c,"is the winner!!")
            if p6=="scissor":
                print(a,"is the winner!!")
        else:
            if p5=="paper":
                if p6=="rock":
                    print(a,"is the winner!!")
                if p6=="scissor":
                    print(c,"is the winner!!")
            else:
                if p5=="scissor":
                    if p6=="paper":
                        print(a,"is the winner!!")
                    if p6=="rock":
                        print(c,"is the winner!!")
                else:
                    print("Wrong input") 

