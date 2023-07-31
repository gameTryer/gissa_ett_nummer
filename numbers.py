import msvcrt
import random

def paus():
    msvcrt.getch()

def minmax_check():
    min_ges = int(input("Enter the minimum number: "))
    max_ges = int(input("Enter the maximum number: "))
    if min_ges == max_ges:
        print("The minimum and maximum guesses cannot be the same. Please try again.")
        minmax_check()
    return min_ges, max_ges

def normal():
    min_ges, max_ges = minmax_check()
    s_ges = random.randint(min_ges, max_ges)
    i = 0
    while True:
        try:
            i_ges = int(input("Guess a number: "))
        except ValueError:
            print("Please enter an integer!")
            continue
        if i_ges == s_ges:
            print(f"Congratulations, you guessed {s_ges} and it took you {i+1} attempts.")
            print("Press any key to continue...")
            paus()
            break
        elif i_ges < s_ges:
            print("Higher.")
            i += 1
        elif i_ges > s_ges:
            print("Lower.")
            i += 1

def challenge():
    min_ges, max_ges = minmax_check()
    s_ges = random.randint(min_ges, max_ges)
    i = 0
    j = 0
    interval = int(input("Enter how often the random number should change (in number of guesses): "))
    while True:
        try:
            i_ges = int(input("Guess a number: "))
        except ValueError:
            print("Please enter an integer!")
            continue
        if i_ges == s_ges:
            print(f"Congratulations, you guessed {s_ges} and it took you {i+1} attempts. The number changed {j+1} times.")
            print("Press any key to continue...")
            paus()
            break
        elif i_ges < s_ges:
            print("Higher.")
            i += 1
        elif i_ges > s_ges:
            print("Lower.")
            i += 1

while True:
    print("Choose game mode:")
    print("1. Normal Mode")
    print("2. Challenge Mode")
    print("0. Exit")
    try:
        c = int(input("Select game mode: "))
        if c == 1:
            normal()
        elif c == 2:
            challenge()
        elif c == 0:
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Not supported in this menu.")
