import msvcrt
import random
def paus():
    msvcrt.getch()
def minmax_check():
    min_ges = int(input("Ange lägsta nummer."))
    max_ges = int(input("Ange högsta nummer."))
    if min_ges == max_ges:
        print("lägsta och högsta gissning får inte vara sama. försök igen")
        return minmax_check() 
    return min_ges, max_ges
    minmax_check() 
    return min_ges, max_ges

def normal():
    min_ges, max_ges = minmax_check()
    s_ges = random.randint(min_ges,max_ges)
    i = 0
    while True:
        try:
            i_ges = int(input("gissa ett nummer"))
        except ValueError:
            print("Ange ett heltal!")
        continue
        if i_ges == s_ges:   
            print("kan gratulera, du gissade på "+str(s_ges)," och det tog"+str(i+1),"gånger")
            print("tryck på en tangent för att fortsätta")
            paus()
            break
        elif i_ges < s_ges:
            print("högre")
            i = i+1
        elif i_ges > s_ges:
            print("lägre")
            i = i+1
def challenge():
    min_ges, max_ges = minmax_check()
    s_ges = random.randint(min_ges, max_ges)
    i = 0
    interval = int(input("Ange hur ofta det slumpmässiga numret ska ändras (i antal gissningar):"))
    while True:
        try:
            i_ges = int(input("gissa ett nummer"))
        except ValueError:
            print("Ange ett heltal!")
            continue
            if i_ges == s_ges:
                print("kan gratulera, du gissade på "+str(s_ges)," och det tog"+str(i+1),"gånger")
                print("tryck på en tangent för att fortsätta")
                paus()
                break
            elif i_ges < s_ges:
                print("högre")
                i = i+1
            elif i_ges > s_ges:
                print("lägre")
                i = i+1
        if i % interval == 0: # ändrar slumpmässigt nummer var interval:te gång
            s_ges = random.randint(min_ges, max_ges)
while True:
    print("välj spelläge.")
    print("1. Normalt läge")
    print("2. utmanings läge")
    print("0. avsluta")
    c = int(input("välj spelläge"))
    if c == 1:
        normal()
    elif c == 2:
        challenge()
    elif c == 0:
        break
    else:
        print("ojiltigt val")