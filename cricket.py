# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:54:15 2020

@author: Akshay Dattatray Khare
"""
import random
import time
l1=[]
l2=[] 
l3=[]
l4=[]

def Third_Umpire1():
    global A1
    global A2
    time.sleep(3)
    tu = random.randint(0,5)
    if tu == 0 or tu == 2 or tu == 4:
        print("Decision Pending........")
        l1.append(0)
        l2.append(0)
        time.sleep(5)
        print("-----------  OUT !!!  -----------")
        time.sleep(1.5)
        print("The total score of", A1," is",sum(l1)," Runs.")
        print("The score of",A2,"is",sum(l2)," Runs.")
        Umpire()
    else:
        print("Decision Pending........")
        time.sleep(6.5)
        print("-----------  NOT OUT !!!  -----------")
        l1.append(0)
        l2.append(0)
        time.sleep(2)
        player1()
        
def Third_Umpire2():
    global B1
    global B2
    time.sleep(3)
    tu = random.randint(0,5)
    if tu == 0 or tu == 2 or tu == 4:
        print("Decision Pending........")
        l3.append(0)
        l4.append(0)
        time.sleep(5)
        print("-----------  OUT !!!  -----------")
        time.sleep(1.5)
        print("The total score of", B1," is",sum(l3)," Runs.")
        print("The score of",B2,"is",sum(l4)," Runs.")
        Umpire()
    else:
        print("Decision Pending........")
        time.sleep(6.5)
        print("-----------  NOT OUT !!!  -----------")
        l3.append(0)
        l4.append(0)
        time.sleep(2)
        player2()
        

def free_hit2():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4
    free = random.randint(0,9)
    time.sleep(3)
    if free == 5:       
        frlb = random.randint(0,5)
        if frlb == 5:
            frro = random.randint(1,2)
            print("Leg-by "+str(frro)+" runs and.....Run out!!!")
            #run3 = run3 + frro 
            #run4 = run4 + 0
            l3.append(frro)
            l4.append(0)
            time.sleep(2)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        else:
            print("Leg-by "+str(frlb)+ " runs")
            #run3 = run3 + frlb 
            #run4 = run4 + 0
            l3.append(frlb)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        
        
    elif free == 7:
        frwkt = random.randint(0,9)
        if frwkt == 0 or frwkt == 1:
            print("Clean Bowled..... But it's a Free hit!!")
            #run3 = run3 + 0
            #run4 = run4 + 0
            l3.append(0)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif frwkt == 2 or frwkt == 3:
            print("LBW Wicket..... But it's a Free hit!!")
            #run3 = run3 + 0
            #run4 = run4 + 0
            l3.append(0)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif frwkt == 4 or frwkt== 5:
            print("Catch Out..... But it's a Free hit!!")
            #run3 = run3 + 0
            #run4 = run4 + 0
            l3.append(0)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif frwkt == 6 or frwkt == 7:
            print("Wicket by keepering!!!....no benefit of free hit!!")
            #run3 = run3 + 0
            #run4 = run4 + 0
            l3.append(0)
            l4.append(0)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        else:
            frrw = random.randint(0,2)
            if frrw == 0:
                print("It's a Run Out!!!")
            elif frrw == 1 or frrw == 2:
                print(str(frrw)+" runs and..... Run Out!!!")
            #run3 = run3 + frrw
            #run4 = run4 + frrw
            l3.append(frrw)
            l4.append(frrw)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        
        
    elif free == 8:       
        wb = random.randint(0,8)
        if wb == 0 or wb == 6 or wb == 7 or wb == 8:            
            #run3 = run3 + 1
            #run4 = run4 + 0
            l3.append(1)         
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                print("Wide!! Free hit continue!!")
                free_hit2()
        elif wb == 1 or wb == 2 or wb == 3:
            print("Wide and "+str(wb)+" runs!!")
            time.sleep(2)
            #run3 = run3 + wb + 1
            #run4 = run4 + 0
            l3.append(wb + 1)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                print("Free hit Continue!!")
                free_hit2()
        elif wb == 4:
            print("Wide and Four!!")
            time.sleep(2)
            #run3 = run3 + 5
            #run4 = run4 + 0
            l3.append(5)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:        
                print("Free hit Continue!!")
                free_hit2()
        else:
            wk = random.randint(0,3)
            if wk == 0:
                print("Wide and... Wicket by keepering!!")
                #run3 = run3 + 1
                #run4 = run4 + 0
                l3.append(1)
                l4.append(0)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif wk == 1 or wk == 2:
                print("Wide...,"+str(wk)+" run...and....Run out!!")
                #run3 = run3 + wk +1
                #run4 = run4 + 0
                l3.append(wk + 1)
                l4.append(0)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            else:
                print("Wide and..... Run out!!")
                #run3 = run3 + 1
                #run4 = run4 + 0
                l3.append(1)
                l4.append(0)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
                
    elif free == 9:
        time.sleep(2)
        print("Again .....Bowler cross the line!!")
        time.sleep(2)
        no_ball2()
    else:
        print(str(free)+" Runs")
        #run3 = run3 + free
        #run4 = run4 + free
        l3.append(free)
        l4.append(free)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:  
            player2()


def no_ball2():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4
    nb = random.randint(0,7)
    if nb == 5:       
        nblb = random.randint(0,5)
        if nblb == 5:
            nbro = random.randint(1,2)
            print("No ball....and...Leg-by "+str(nbro)+" runs and.....Run out!!!")
            #run3 = run3 + nbro +1
            #run4 = run4 + 0
            l3.append(nbro + 1)
            l4.append(0)
            time.sleep(2)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        else:
            print("No ball....and...Leg-by "+str(nblb)+ " runs")
            time.sleep(2)
            #run3 = run3 + nblb +1
            #run4 = run4 + 0
            l3.append(nblb + 1)
            l4.append(0)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")            
                free_hit2()
    elif nb == 7:
        nbwkt = random.randint(0,9)
        if nbwkt == 0 or nbwkt == 1:
            print("Clean Bowled..... But it's a No Ball!!!")
            #run3 = run3 + 1
            #run4 = run4 + 0
            l3.append(1)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:      
                print("And... Now it's a Free hit!!")
                free_hit2()
        elif nbwkt == 2 or nbwkt == 3:
            print("LBW Wicket..... But it's a No Ball!!")
            #run3 = run3 + 1
            #run4 = run4 + 0
            l3.append(1)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit2()
        elif nbwkt == 4 or nbwkt== 5:
            print("Catch Out..... But it's a No Ball!!")
            #run3 = run3 + 1
            #run4 = run4 + 0
            l3.append(1)
            l4.append(0)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit2()
        elif nbwkt == 6 or nbwkt == 7:
            print("No Ball....But Wicket by keepering!!!")
            #run3 = run3 + 1
            #run4 = run4 + 0
            l3.append(1)
            l4.append(0)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        else:
            nbrw = random.randint(0,2)
            if nbrw == 0:
                print("No Ball....But it's a Run Out!!!")
            elif nbrw == 1 or nbrw == 2:
                print("No Ball...."+str(nbrw)+" runs and..... Run Out!!!")
            #run3 = run3 + nbrw+1
            #run4 = run4 + nbrw
            l3.append(nbrw + 1)
            l4.append(nbrw)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        
    
    else:
        print("No Ball.....and "+str(nb)+" Runs!!!")
        #run3 = run3 + 1 + nb
        #run4 = run4 + nb
        l3.append(1 + nb)
        l4.append(nb)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            print("And... Now it's a Free hit!!")
            free_hit2()

def free_hit1():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4
    free = random.randint(0,9)
    time.sleep(3)
    if free == 5:       
        frlb = random.randint(0,5)
        if frlb == 5:
            frro = random.randint(1,2)
            print("Leg-by "+str(frro)+" runs and.....Run out!!!")
            #run = run + frro 
            #run1 = run1 + 0
            l1.append(frro)
            l2.append(0)
            time.sleep(2)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        else:
            print("Leg-by "+str(frlb)+ " runs")
            #run = run + frlb 
            #run1 = run1 + 0
            l1.append(frlb)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        
        
    elif free == 7:
        frwkt = random.randint(0,9)
        if frwkt == 0 or frwkt == 1:
            print("Clean Bowled..... But it's a Free hit!!")
            #run = run+0
            #run1 = run1 + 0
            l1.append(0)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif frwkt == 2 or frwkt == 3:
            print("LBW Wicket..... But it's a Free hit!!")
            #run = run+0
            #run1 = run1 + 0
            l1.append(0)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif frwkt == 4 or frwkt== 5:
            print("Catch Out..... But it's a Free hit!!")
            #run = run+0
            #run1 = run1 + 0
            l1.append(0)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif frwkt == 6 or frwkt == 7:
            print("Wicket by keepering!!!....no benifit of free hit!!")
            #run = run+0
            #run1 = run1 + 0
            l1.append(0)
            l2.append(0)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        else:
            frrw = random.randint(0,2)
            if frrw == 0:
                print("It's a Run Out!!!")
            elif frrw == 1 or frrw == 2:
                print(str(frrw)+" runs and..... Run Out!!!")
            #run = run + frrw
            #run1 = run1 + frrw
            l1.append(frrw)
            l2.append(frrw)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        
        
    elif free == 8:       
        wb = random.randint(0,8)
        if wb == 0 or wb == 6 or wb == 7 or wb == 8:
            
            #run = run +1
            #run1 = run1 + 0
            l1.append(1)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("Wide!! Free hit continue!!")
                free_hit1()
        elif wb == 1 or wb == 2 or wb == 3:
            print("Wide and "+str(wb)+" runs!!")
            time.sleep(2)
            
            #run = run +wb+1
            #run1 = run1 + 0
            l1.append(wb + 1)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("Free hit Continue!!")
                free_hit1()
        elif wb == 4:
            print("Wide and Four!!")
            time.sleep(2)
            #run = run + 5
            #run1 = run1+0
            l1.append(5)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("Free hit Continue!!")
                free_hit1()
        else:
            wk = random.randint(0,3)
            if wk == 0:
                print("Wide and... Wicket by keepering!!")
                #run = run + 1
                #run1 = run1 + 0
                l1.append(1)
                l2.append(0)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            elif wk == 1 or wk == 2:
                print("Wide...,"+str(wk)+" run...and....Run out!!")
                #run = run + wk +1
                #run1 = run1 + 0
                l1.append(wk + 1)
                l2.append(0)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            else:
                print("Wide and..... Run out!!")
                #run = run + 1
                #run1 = run1 + 0
                l1.append(1)
                l2.append(0)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
                
    elif free == 9:
        time.sleep(2)
        print("Again ....Bowler cross the line!!")
        time.sleep(1.5)
        no_ball1()
    else:
        print(str(free)+" Runs")
        #run = run + free
        #run1 = run1 + free
        l1.append(free)
        l2.append(free)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()

def no_ball1():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4
    nb = random.randint(0,7)
    time.sleep(2.2)
    if nb == 5:       
        nblb = random.randint(0,5)
        if nblb == 5:
            nbro = random.randint(1,2)
            print("No ball...and....Leg-by "+str(nbro)+" runs and.....Run out!!!")
            #run = run + nbro +1
            #run1 = run1 + 0
            l1.append(nbro + 1)
            l2.append(0)
            time.sleep(2)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        else:
            print("No ball....and...Leg-by "+str(nblb)+ " runs")
            time.sleep(2)            
            #run = run + nblb +1
            #run1 = run1 + 0
            l1.append(nblb + 1)
            l2.append(0)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit1()
    elif nb == 7:
        nbwkt = random.randint(0,9)
        if nbwkt == 0 or nbwkt == 1:
            print("Clean Bowled..... But it's a No Ball!!!")
            #run = run+1
            #run1 = run1 + 0
            l1.append(1)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit1()
        elif nbwkt == 2 or nbwkt == 3:
            print("LBW Wicket..... But it's a No Ball!!")
            #run = run+1
            #run1 = run1 + 0
            l1.append(1)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit1()
        elif nbwkt == 4 or nbwkt== 5:
            print("Catch Out..... But it's a No Ball!!")
            #run = run+1
            #run1 = run1 + 0
            l1.append(1)
            l2.append(0)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                print("And... Now it's a Free hit!!")
                free_hit1()
        elif nbwkt == 6 or nbwkt == 7:
            print("No Ball....But Wicket by keepering!!!")
            #run = run+1
            #run1 = run1 + 0
            l1.append(1)
            l2.append(0)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        else:
            nbrw = random.randint(0,2)
            if nbrw == 0:
                print("No Ball....But it's a Run Out!!!")
            elif nbrw == 1 or nbrw == 2:
                print("No Ball...."+str(nbrw)+" runs and..... Run Out!!!")
            #run = run + nbrw+1
            #run1 = run1 + nbrw
            l1.append(nbrw + 1)
            l2.append(nbrw)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        
    
    else:
        print("No Ball.....and "+str(nb)+" Runs!!!")
        #run = run+1+nb
        #run1 = run1 + nb
        l1.append(1 + nb)
        l2.append(nb)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            print("And... Now it's a Free hit!!")
            free_hit1()

def Umpire():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4 
    r1 = sum(l1)+1
    r3 = sum(l3)+1
    time.sleep(2)
    if sum(l1)==0 and sum(l2)==0 and l1==[] and l2==[]:
        #print("Extra runs: ",sum(l1)-sum(l2))
        print("Target for "+A1+" is "+str(r3)+" runs!!")
        time.sleep(3.5)
        print("Now "+A1+" will start the second innings")
        print(" ")
        player1()
    elif sum(l3)==0 and sum(l4)==0 and l3==[] and l4==[]:
        #print("Extra runs: ",sum(l1)-sum(l2))        
        print("Target for "+B1+" is "+str(r1)+" runs!!")
        time.sleep(3.5)
        print("Now "+B1+" will start the second innings")
        print(" ")
        player2()
        
    if sum(l1) > sum(l3):
        print(A1,"Won the match!!")
        print("Here is the trophy...")
        print("..........")
        print(".        .")
        print(" .      . ")
        print("  .    .  ")
        print("   .  .   ")
        print("    ..    ")
        print("    ..    ")
        print("   ....   ")
        print("  ......  ")
        print(" ")
        print(f"Congratulations to the winning team {A1}!!")
        
        
        
    elif sum(l3) > sum(l1):
        print(B1," Won the match!!")
        print("Here is the trophy...")
        print("..........")
        print(".        .")
        print(" .      . ")
        print("  .    .  ")
        print("   .  .   ")
        print("    ..    ")
        print("    ..    ")
        print("   ....   ")
        print("  ......  ")
        print(" ")
        print(f"Congratulations to the winning team {B1}!!")
        
    else:
        print("Match Tied!!")
    #print(l1)
    #print(l2)
    #print(l3)
    #print(l4)
        
def player1():
    global A1
    global A2
    global B1
    global B2  
    global run
    global run1
    global run3
    global run4
    run = 0
    run1 = 0
    A = random.randint(0,17)
    time.sleep(2)
    if A == 7:
        wkt = random.randint(0,9)
        if wkt == 0 or wkt == 1:
            print("Clean Bowled!!!")
            run = run+0
            run1 = run1 + 0
            l1.append(run)
            l2.append(run1)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        elif wkt == 2 or wkt == 3:
            if wkt == 2:
                print("LBW Wicket!!")
                run = run+0
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
                
            elif wkt == 3:
                print("There is a appeal for LBW Wicket!!")
                time.sleep(3)
                print("The decision will be taken by third umpire.")
                Third_Umpire1()
        elif wkt == 4 or wkt== 5:
            if wkt == 4:
                print("Catch Out!!")
                run = run+0
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            elif wkt == 5:
                print("There is a appeal for catch out by wicket keeper!!")
                time.sleep(3)
                print(" Wicket keeper says that ball touched to the bat.")
                time.sleep(3)
                print("The decision will be taken by third umpire.")
                Third_Umpire1()
                
        elif wkt == 6 or wkt == 7:
            if wkt == 6:
                print("Wicket by keepering!!! Batsman's leg not in the creeze and wicket kepper took benefit of it.")
                time.sleep(4.5)
                run = run+0
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            elif wkt == 7:
                print("There is a appeal. Batsman's leg may or may not be in the creeze and wicket kepper took benefit of it.")
                time.sleep(4.5)
                print("The decision will be taken by third umpire.")
                Third_Umpire1()
        else:
            rw = random.randint(0,2)
            if rw == 0:
                print("Run Out!!!")
                run = run+0
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            elif rw == 1 or rw == 2:
                print(str(rw)+" runs and..... Run Out!!!")
                run = run + rw
                run1 = run1 + rw
                l1.append(run)
                l2.append(run1)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
        
    elif A == 5:
        wb = random.randint(0,8)
        if wb == 0 or wb == 6 or wb == 7 or wb == 8:
            print("Wide!!")
            run = run +1
            run1 = run1 + 0
            l1.append(run)
            l2.append(run1)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif wb == 1 or wb == 2 or wb == 3:
            print("Wide and "+str(wb)+" runs!!")
            run = run +wb+1
            run1 = run1 + 0
            l1.append(run)
            l2.append(run1)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif wb == 4:
            print("Wide and Four!!")
            run = run + 5
            run1 = run1+0
            l1.append(run)
            l2.append(run1)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        else:
            wk = random.randint(0,3)
            if wk == 0:
                print("Wide and... Wicket by keepering!!")
                run = run + 1
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            elif wk == 1 or wk == 2:
                print("Wide...,"+str(wk)+" run...and....Run out!!")
                run = run + wk +1
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
            else:
                print("Wide and..... Run out!!")
                run = run + 1
                run1 = run1 + 0
                l1.append(run)
                l2.append(run1)
                time.sleep(2)
                print("The total score of", A1," is",sum(l1)," Runs.")
                print("The score of",A2,"is",sum(l2)," Runs.")
                Umpire()
                
                
    elif A == 4 or A == 11:
        print("Four!!")
        run = run+4
        run1 = run1 + 4
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()
    elif A == 6 or A == 12:
        print("Six!!")
        run = run+6
        run1 = run1 + 6
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()
    elif A == 0 or A == 10 or A == 14:
        print("Dot ball")
        run = run+0
        run1 = run1 + 0
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()
    elif A == 8:
        lb = random.randint(1,5)
        if lb == 5:
            lw = random.randint(1,2)
            print("Leg-by "+str(lw)+" runs and.....Run out!!!")
            run = run + lw
            run1 = run1 + 0
            l1.append(run)
            l2.append(run1)
            time.sleep(2)
            print("The total score of", A1," is",sum(l1)," Runs.")
            print("The score of",A2,"is",sum(l2)," Runs.")
            Umpire()
        else:
            print("Leg-by "+str(lb)+ " runs")
            run = run + lb
            run1 = run1 + 0
            l1.append(run)
            l2.append(run1)
            time.sleep(2)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
    
    elif A == 9:
        no_ball1()
        
    elif A == 13:
        otr = random.randint(0,5)
        if otr == 0 or otr == 5:
            print("2 Runs and...another 2 runs bacause of overthrow!!")
            time.sleep(4)
            l1.append(4)
            l2.append(4)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
        elif otr == 1 or otr == 2 or otr == 3:
            print(otr," runs and... another 4 runs because of overthrow!!")
            time.sleep(4)
            l1.append(otr + 4)
            l2.append(otr + 4)
            if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                print(A2," scored ",sum(l2)," runs!!")
                print(A1," won th match!!")
            else:
                player1()
            
        elif otr == 4:
            wball = random.randint(4,5)
            if wball == 5:
                wn = random.randint(1,3)
                print("No ball and....",wn," runs and another 4 runs because of overthrow!!")
                time.sleep(4)
                l1.append(1 + wn + 4)
                l2.append(wn + 4)
                if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                    print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                    print(A2," scored ",sum(l2)," runs!!")
                    print(A1," won th match!!")
                else:
                    free_hit1()
            elif wball == 4:
                wor = random.randint(1,3)
                print("Wide ball....",wor," runs and....another 4 runs because of overthrow!!! ")
                time.sleep(4)
                l1.append(wor + 5)
                l2.append(0)
                if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
                    print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
                    print(A2," scored ",sum(l2)," runs!!")
                    print(A1," won th match!!")
                else:
                    player1()
    
                  
    elif A == 1 or A == 15 or A == 17:
        print("1 run")
        run = run + 1
        run1 = run1 + 1
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()
            
    elif A == 2 or A == 16:
        print("2 runs")
        run = run + 2
        run1 = run1 + 2
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()
            
    elif A == 3:
        print("3 runs")
        run = run + 3
        run1 = run1 + 3
        l1.append(run)
        l2.append(run1)
        time.sleep(2)
        if l3 != [] and l4 != [] and sum(l1) > sum(l3) :
            print(A1," chase the target given by ",B1, " and scored ",sum(l1)," runs!!")
            print(A2," scored ",sum(l2)," runs!!")
            print(A1," won th match!!")
        else:
            player1()



def player2():
    global A1
    global A2
    global B1
    global B2
    global run
    global run1
    global run3
    global run4
    run3 = 0
    run4 = 0
    
    A = random.randint(0,17)
    time.sleep(2)
    if A == 7:
        wkt = random.randint(0,9)
        if wkt == 0 or wkt == 1:
            print("Clean Bowled!!!")
           
            run3 = run3 + 0
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        elif wkt == 2 or wkt == 3:
            if wkt == 2:
                print("LBW Wicket!!")
                run3 = run3 + 0
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif wkt == 3:
                print("There is a appeal for LBW Wicket!!")
                time.sleep(3)
                print("The decision will be taken by third umpire.")
                Third_Umpire2()
        elif wkt == 4 or wkt== 5:
            if wkt == 4:
                print("Catch Out!!")
                run3 = run3 + 0
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif wkt == 5:
                print("There is a appeal for catch out by wicket keeper!!")
                time.sleep(3)
                print(" Wicket keeper says that ball touched to the bat.")
                time.sleep(3)
                print("The decision will be taken by third umpire.")
                Third_Umpire2()
                
        elif wkt == 6 or wkt == 7:
            if wkt == 6:
                print("Wicket by keepering!!! Batesman's leg not in the creeze and wicket kepper took benefit of it.")
                time.sleep(5)
                run3 = run3 + 0
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif wkt == 7:
                print("There is a appeal. Batesman's leg may or may not be in the creeze and wicket kepper took benefit of it.")
                time.sleep(5)
                print("The decision will be taken by third umpire.")
                Third_Umpire2()
        else:
            rw = random.randint(0,2)
            if rw == 0:
                print("Run Out!!!")
                run3 = run3 + 0
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif rw == 1 or rw == 2:
                print(str(rw)+" runs and..... Run Out!!!")
                run3 = run3 + rw
                run4 = run4 + rw
                l3.append(run3)
                l4.append(run4)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()

    elif A == 5:
        wb = random.randint(0,8)
        if wb == 0 or wb == 6 or wb == 7 or wb == 8:
            print("Wide!!")
            run3 = run3 +1
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif wb == 1 or wb == 2 or wb == 3:
            print("Wide and "+str(wb)+" runs!!")
            run3 = run3 +wb+1
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif wb == 4:
            print("Wide and Four!!")
            run3 = run3 + 5
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        else:
            wk = random.randint(0,3)
            if wk == 0:
                print("Wide and... Wicket by keepering!!")
                run3 = run3 + 1
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            elif wk == 1 or wk == 2:
                print("Wide...,"+str(wk)+" run...and....Run out!!")
                run3 = run3 + wk +1
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
            else:
                print("Wide and..... Run out!!")
                run3 = run3 + 1
                run4 = run4 + 0
                l3.append(run3)
                l4.append(run4)
                time.sleep(2)
                print("The total score of", B1," is",sum(l3)," Runs.")
                print("The score of",B2,"is",sum(l4)," Runs.")
                Umpire()
    elif A == 4 or A == 11:
        print("Four!!")
        run3 = run3+4
        run4 = run4 + 4
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()
    elif A == 6 or A == 12:
        print("Six!!")
        run3 = run3+6
        run4 = run4 + 6
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()
    elif A == 0 or A == 10 or A == 14:
        print("Dot ball")
        run3 = run3+0
        run4 = run4 + 0
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()
    elif A == 8:
        lb = random.randint(1,5)
        if lb == 5:
            lw = random.randint(1,2)
            print("Leg-by "+str(lw)+" runs and.....Run out!!!")
            run3 = run3 + lw
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            time.sleep(2)
            print("The total score of", B1," is",sum(l3)," Runs.")
            print("The score of",B2,"is",sum(l4)," Runs.")
            Umpire()
        else:
            print("Leg-by "+str(lb)+ " runs")
            run3 = run3 + lb
            run4 = run4 + 0
            l3.append(run3)
            l4.append(run4)
            time.sleep(2)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
            
    elif A == 9:
        no_ball2()
        
    elif A == 13:
        otr = random.randint(0,5)
        if otr == 0 or otr == 5:
            print("2 Runs and...another 2 runs bacause of overthrow!!")
            time.sleep(4)
            l3.append(4)
            l4.append(4)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
        elif otr == 1 or otr == 2 or otr == 3:
            print(otr," runs and... another 4 runs because of overthrow!!")
            time.sleep(4)
            l3.append(otr + 4)
            l4.append(otr + 4)
            if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                print(B2," scored ",sum(l4)," runs!!")
                print(B1," won th match!!")
            else:
                player2()
            
        elif otr == 4:
            wball = random.randint(4,5)
            if wball == 5:
                wn = random.randint(1,3)
                print("No ball and....",wn," runs and another 4 runs because of overthrow!!")
                time.sleep(4)
                l3.append(1 + wn + 4)
                l4.append(wn + 4)
                if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                    print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                    print(B2," scored ",sum(l4)," runs!!")
                    print(B1," won th match!!")
                else:
                    free_hit2()
            elif wball == 4:
                wor = random.randint(1,3)
                print("Wide ball....",wor," runs and....another 4 runs because of overthrow!!! ")
                time.sleep(4)
                l3.append(wor + 5)
                l4.append(0)
                if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
                    print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
                    print(B2," scored ",sum(l4)," runs!!")
                    print(B1," won th match!!")
                else:
                    player2()
    
    elif A == 1 or A == 15 or A == 17:
        print("1 run")
        run3 = run3 + 1
        run4 = run4 + 1
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()
            
    elif A == 2 or A == 16:
        print("2 runs")
        run3 = run3 + 2
        run4 = run4 + 2
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()
            
    elif A == 3:
        print("3 runs")
        run3 = run3 + 3
        run4 = run4 + 3
        l3.append(run3)
        l4.append(run4)
        time.sleep(2)
        if l1 != [] and l2 != [] and sum(l3) > sum(l1) :
            print(B1," chase the target given by ",A1, " and scored ",sum(l3)," runs!!")
            print(B2," scored ",sum(l4)," runs!!")
            print(B1," won th match!!")
        else:
            player2()


print("Welcome!!")
A1=input("Enter team name:")
A2=input("Enter Player's name of "+A1+":")
B1=input("Enter another team's name:")
B2=input("Enter player's name of "+B1+":")
time.sleep(2)
print("It's a time of toss!!.")
time.sleep(2)
select = random.randint(0,1)
if select == 0:
    print(A1," will select the toss!!")
    time.sleep(2)
    a=input("What do you want to choose head or tail?")
    a=a.upper().strip()[0]
    time.sleep(2)
    toss1=random.randint(0,1)
    if toss1 == 0:
        toss1 = "H"
        print("Head!!")
    else:
        toss1 = "T"
        print("Tail!!")
    
    if a == toss1:
        print(A1," won the toss!!")
        time.sleep(2)
        bat_bowl=input("What do you want to choose? Batting or Fielding?")
        bat_bowl = bat_bowl.upper().strip()[0]
        time.sleep(1)
        if bat_bowl=="B":
            print(A1," choose batting.")
        else:
            print(A1," choose fielding.")
        time.sleep(2)
        print("Let us start the cricket!!")
        time.sleep(1.65)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Go!!")
        print(" ")
        time.sleep(3)
        if bat_bowl=="B":
            player1()
        else:
            player2()
    else:
        print(B1," won the toss!!")
        time.sleep(2)
        bat_bowl=input("What do you want to choose? Batting or Fielding?")
        bat_bowl = bat_bowl.upper().strip()[0]
        time.sleep(1)
        if bat_bowl=="B":
            print(B1," choose batting.")
        else:
            print(B1," choose fielding.")
        time.sleep(2)
        print("Let us start the cricket!!")
        time.sleep(1.65)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Go!!")
        print(" ")
        print("--------------------------------------")
        print(" ")
        time.sleep(3)
        if bat_bowl=="B":
            player2()
        else:
            player1()
else:
    print(B1," will selects the toss!!")
    time.sleep(2)
    b=input("What do you want to choose head or tail?")
    b=b.upper().strip()[0]
    time.sleep(2)
    toss2=random.randint(0,1)
    if toss2 == 0:
        toss2 = "H"
        print("Head!!")
    else:
        toss2 = "T"
        print("Tail!!")
    
    if b == toss2:
        print(B1," won the toss!")
        time.sleep(2)
        bat_bowl=input("What do you want to choose? Batting or Fielding?")
        bat_bowl = bat_bowl.upper().strip()[0]
        time.sleep(1)
        if bat_bowl=="B":
            print(B1," choose batting.")
        else:
            print(B1," choose fielding.")
        time.sleep(2)
        print("Let us start the cricket!!")
        time.sleep(1.65)
        print("3")
        time.sleep(1)       
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Go!!")
        print(" ")
        print("--------------------------------------")
        print(" ")
        time.sleep(3)
        if bat_bowl=="B":
            player2()
        else:
            player1()
    else:
        print(A1," won the toss!!")
        time.sleep(2)
        bat_bowl=input("What do you want to choose? Batting or Fielding?")
        bat_bowl = bat_bowl.upper().strip()[0]
        time.sleep(1)
        if bat_bowl=="B":
            print(A1," choose batting.")
        else:
            print(A1," choose fielding.")
        
        time.sleep(2)
        print("Let us start the cricket!!")
        time.sleep(1.65)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Go!!")
        print(" ")
        print("--------------------------------------")
        print(" ")
        time.sleep(3)
        if bat_bowl == "B":
            player1()
        else:
            player2()
        

    
    
    
    
    
