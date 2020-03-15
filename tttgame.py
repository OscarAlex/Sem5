"""
Created on Tue Nov 19 14:42:29 2019
@author: Oscar
"""
#from tictac import prepDatos
from sklearn.tree import DecisionTreeClassifier
trainF, testF, trainL, testL= prepDatos()
#from random import randrange
import random
dtree= DecisionTreeClassifier()
dtree.fit(trainF,trainL)
tab= [2,2,2,2,2,2,2,2,2]

def imprTab(tab):
    vals= []
    for i in range(9):
        if(tab[i] == 2):
            vals.append(' ')
        if(tab[i] == 1):
            vals.append('X')
        if(tab[i] == 0):
            vals.append('O')
    print('       ', vals[0], '\N{SUPERSCRIPT ONE}',' | ', vals[1], '\N{SUPERSCRIPT TWO}', ' | ', vals[2], '\N{SUPERSCRIPT THREE}')
    print('      -----------------')
    print('       ', vals[3], '\N{SUPERSCRIPT FOUR}',' | ', vals[4], '\N{SUPERSCRIPT FIVE}', ' | ', vals[5], '\N{SUPERSCRIPT SIX}')
    print('      -----------------')
    print('       ', vals[6], '\N{SUPERSCRIPT SEVEN}',' | ', vals[7], '\N{SUPERSCRIPT EIGHT}', ' | ', vals[8], '\N{SUPERSCRIPT NINE}')


def jugador():
    imprTab(tab)
    try:
        while True:
            pos= int(input("Introduce una posición entre 1-9\N{SUPERSCRIPT THREE}: "))
            print('\n\n\n\n\n\n\n')
            if(pos>0 and pos<10):
                if(tab[pos-1] == 2):
                    tab[pos-1]= 1
                    break
                else:
                    print("Posición ocupada")
                    imprTab(tab)
            else:
                print("Recuerda, entre 1-9")
                imprTab(tab)
    except:
        print('\n\n\n\n\n\n\n')
        print("Introduce un número")


def IA():
    """
    clas= dtree.predict([tab])
    if(clas):
        while True:
            ran= random.randint(0,8)
            if(tab[ran] == 2):
                tab[ran]= 0
                break
    print(clas)
    """
    pseboards= []
    tmptab= tab.copy()
    for i in range(9):
        if(tab[i] == 2):
            tmptab[i]= 0
            pseboards.append(tmptab)
            print(tmptab,'\n')
            tmptab= tab.copy()
    
    preboards=[]
    for i in range(len(pseboards)):
        c= dtree.predict([pseboards[i]])
        preboards.append(c)
        print(c,'\n')

def terminar():
    tmp= bool(1)
    if((tab[0]==1 and tab[3]==1 and tab[6]==1) or #Vertical
       (tab[1]==1 and tab[4]==1 and tab[7]==1) or
       (tab[2]==1 and tab[5]==1 and tab[8]==1) or
       (tab[0]==1 and tab[1]==1 and tab[2]==1) or #Horizontal
       (tab[3]==1 and tab[4]==1 and tab[5]==1) or
       (tab[6]==1 and tab[7]==1 and tab[8]==1) or
       (tab[0]==1 and tab[4]==1 and tab[8]==1) or #Diagonal
       (tab[6]==1 and tab[4]==1 and tab[2]==1)):
        tmp= bool(0)
        print("Has ganado")
    elif((tab[0]==0 and tab[3]==0 and tab[6]==0) or #Vertical
       (tab[1]==0 and tab[4]==0 and tab[7]==0) or
       (tab[2]==0 and tab[5]==0 and tab[8]==0) or
       (tab[0]==0 and tab[1]==0 and tab[2]==0) or #Horizontal
       (tab[3]==0 and tab[4]==0 and tab[5]==0) or
       (tab[6]==0 and tab[7]==0 and tab[8]==0) or
       (tab[0]==0 and tab[4]==0 and tab[8]==0) or #Diagonal
       (tab[6]==0 and tab[4]==0 and tab[2]==0)):
        tmp= bool(0)
        print("Has perdido")
    elif(tab[0]!=2 and tab[1]!=2 and tab[2]!=2 and 
       tab[3]!=2 and tab[4]!=2 and tab[5]!=2 and 
       tab[6]!=2 and tab[7]!=2 and tab[8]!=2):
        tmp= bool(0)
        print("Empate")
    return tmp


print('\n\n\n')
while terminar():
    #imprTab(tab)
    jugador()
    IA()
imprTab(tab)

