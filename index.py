import random
from getpass import getpass

p1_name=input("Enter your name ")
print("Bot: Hi",p1_name,"!")
print("Bot: Ready to play rock ,paper and scissors !")
print("Bot: There are two modes")
print("Bot: Bot vs Player(1st) and Player1 vs Player2(2nd)")
print("Bot: To play 1st mode enter (c)and to play second mode enter any string(letters)")
mode=input(p1_name+": ")
mode=mode.lower()
p2=""
p2_name=""
winner_name=""
if mode=="c":
    l=["rock","paper","scissor"]
    p2_name="Bot"
    print("Bot: I have entered ,it's your turn")
    p2=random.choice(l)
else:
    p2_name=input("Bot: Enter second player name ")
    p2=input(p2_name+": ")
    p2=p2.lower()
p1=input(p1_name+": ")
p1=p1.lower() 
if p1!="paper" and p1!="rock" and p1!="scissor" or p2!="paper" and p2!="rock" and p2!="scissor":
    print("wrong input")
else:
    if(p1==p2):
        print("Game tied!!")
    else:
        if p2=="rock":
            if p1=="paper":
                winner_name=p1_name
            if p1=="scissor":
                winner_name=p2_name
        else:
            if p2=="paper":
                if p1=="rock":
                    winner_name=p2_name
                if p1=="scissor":
                    winner_name=p1_name
            else:
                if p2=="scissor":
                    if p1=="rock":
                        winner_name=p1_name
                    if p1=="paper":
                        winner_name=p2_name
print(winner_name,"is the winner!!")
