import random
from getpass import getpass

def rps(p1,p2):
    if p1!="paper" and p1!="rock" and p1!="scissor" or p2!="paper" and p2!="rock" and p2!="scissor":
        return 1
    else:
        if(p1==p2):
            return 2
        else:
            if p2=="rock":
                if p1=="paper":
                    return 3
                if p1=="scissor":
                    return 4        
            else:
                if p2=="paper":
                    if p1=="rock":
                        return 4  
                    if p1=="scissor":
                        return 3
                else:
                    if p2=="scissor":
                        if p1=="rock":
                            return 3 
                        if p1=="paper":
                            return 4
                            
                            
p1_name=input("Enter your name ")
print("Bot: Hi",p1_name,"!")
print("Bot: Ready to play rock ,paper and scissors !")
true=input(p1_name+": ")
true=true.lower()
if true=="yes" or true=="y":
    while true:
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
            p2=getpass(p2_name+": ")
            p2=p2.lower()
        p1=input(p1_name+": ")
        p1=p1.lower()
        result=rps(p1,p2)
        if result==1:
            print("Wrong input")
        elif result==2:
            print("Game tied")
        elif result==3:
            print(p1_name,"is the winner!!")
        else:
            print(p2_name,"is the winner!!")
        print("Bot: Do you want to play again",p1_name)
        print("Bot: for yes(y) and for no(n)")
        ag=input(p1_name+": ")
        ag=ag.lower()
        if ag=="yes" or ag=="y":
            print("Bot: Ok")
        else:
            print("Bot: Ok, we'll play next time if you want")
            break
elif true=="no" or true=="n":
    print("Bot: Ok, we'll play next time if you want")
else:
    print("invalid string",p1_name)
           
