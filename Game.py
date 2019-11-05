import DatabaseOrg 
import time 
import random





def Playgame(count):
    count=int (count)
    play=True 
    timeend=time.time()+60
    while(play==True):
        over=True 
        while (over==True):
            word=random.choice(DatabaseOrg.list_words)
            unspeakable=[]
            unspeakable=DatabaseOrg.dict_unspeakable[word]
            print ("------",word,"------")
            for i in unspeakable:
                x="--"+i+"--"
                print (x,end=",")
            print ()
            print ("1.Correct")
            print ("2.Pass")
            print ("3.Taboo")
            r=int(input())
            if r == 1 :
                count+=1
            elif r == 2:
                count+=1
                count-=1
            elif r==3 :
                count-=1
            if time.time()>=timeend:
                over=False 
                play=False
                

    return count 

def main():
    print ("1.Play Game")
    print ("2.Exit")
    n=int(input()) 
    scoreA=0
    tempA=0
    tempB=0
    scoreB=0
    finish=False 
    while finish==False: 
        if n==1:
            print ("Team A: Press 1 when ready")
            l1=int(input())
            if l1 == 1   :
                print("Team A Starts")
                tempA=Playgame(scoreA)
            print ("Team B: Press 1 when ready")
            l2=int(input())
            if l2 == 1   :
                print("Team B starts")
                tempB=Playgame(scoreB)
            scoreA=tempA
            scoreB=tempB
            print ("Team A:",scoreA,"Team B:", scoreB)
            print ("1.Continue")
            print ("2.Over")
            x=int(input())
            if x==1:
                continue
            else:
                print ("Final Score")
                print ("Team A:",scoreA," Team B:", scoreB)
                finish=True 
        else : 
            exit()


main ()



