import time

#gets the desired width from the user (more like half max width since it's *2 but eh)
x = True
while x:
    try:
        width = abs(int(input("Enter width: ")))
        if width <= 1:
            y = int("yes")
        else: 
            x = False
    except:
        print("Enter an integer more than 1.") #if user enters non-integer, prints this and repeats the question

#gets the desired character for the pattern
x = True
while x:
    middle = input("Enter character for middle pattern: ")
    if len(middle) == 1: #don't want the width to get too wide, so limit it to one character
        x = False
    else: 
        print("Enter a single charater.")

#gets the desired character for the pattern
x = True
while x:
    sides = input("Enter character for side pattern: ")
    if len(sides) == 1: #don't want the width to get too wide, so limit it to one character
        x = False
    else: 
        print("Enter a single charater.")

#desired scrolling speed
x = True
while x:
    try:
        speed = abs(int(input("Enter speed 1-10: "))) #1 = slowest speed, 10 = fastest speed
        if speed == 0:
            nonsense = int("yes")
        elif speed <= 10:
            x = False
    except:
        print("Enter an integer.")
speed = 0.1/speed #have to get an inverse value because of how the time.sleep takes the interval of time instead.


while True:

############################################################### Expanding time

    for i in range(1, width):
        x = width - i
        if x%2 == 1:#for the first iteration of patterns, starts with "##"
            while x >= 4:#prints the major chunk of the side patters in blocks of "##  "
                print(2*sides + 2*" ", end="")
                x -= 4
            if x == 3:#Remainders are printed according to how many spaces are leftover
                print(2*sides + " ", end="")
            elif x == 2:
                print(2*sides, end="")
            elif x == 1:
                print(sides, end="")

        elif x%2 == 0:
            while x >= 4:#for the second iteration of patterns, starts with "  "
                print(2*" " + 2*sides, end="")
                x -= 4
            if x == 3:
                print(2*" " + sides, end="")
            elif x == 2:
                print(2*" ", end="")
            elif x == 1:
                print(" ", end="")

        print(middle*2*i, end="") #middle pattern! so simple lol

        x = width - i
        if x%2 == 1:#for the right side of patterns
            if x%4 == 3:#have to start with checking the remainders cus the pattern starts immediately after the middle pattern
                print(" " + 2*sides, end="")#   i.e. each line does not start at the same space, unlike the left pattern
                x -= 3
            elif x%4 == 2:
                print(2*sides, end="")
                x -= 2
            elif x%4 == 1:
                print(sides, end="")
                x -= 1
            while x >= 4:#once the remainders have been dealt with, can now print the majority of the pattern in blocks of "  ##"
                print(2*" " + 2*sides, end="")
                x -= 4
            print()

        elif x%2 == 0:
            if x%4 == 3:
                print(sides + 2*" ", end="")
                x -= 3
            elif x%4 == 2:
                print(2*" ", end="")
                x -= 2
            elif x%4 == 1:
                print(" ", end="")
                x -= 1
            while x >= 4:
                print(2*sides + 2*" ", end="")
                x -= 4
            print()

        time.sleep(speed)

############################################################### Shrinking time

    for i in range(width, 1, -1): #shrink
        x = width - i
        if x%2 == 1:
            while x >= 4:
                print(2*sides + 2*" ", end="")
                x -= 4
            if x == 3:
                print(2*sides + " ", end="")
            elif x == 2:
                print(2*sides, end="")
            elif x == 1:
                print(sides, end="")

        elif x%2 == 0:
            while x >= 4:
                print(2*" " + 2*sides, end="")
                x -= 4
            if x == 3:
                print(2*" " + sides, end="")
            elif x == 2:
                print(2*" ", end="")
            elif x == 1:
                print(" ", end="")


        print(middle*2*i, end="") #middleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

        x = width - i
        if x%2 == 1:
            if x%4 == 3:
                print(" " + 2*sides, end="")
                x -= 3
            elif x%4 == 2:
                print(2*sides, end="")
                x -= 2
            elif x%4 == 1:
                print(sides, end="")
                x -= 1
            while x >= 4:
                print(2*" " + 2*sides, end="")
                x -= 4
            print()

        elif x%2 == 0:
            if x%4 == 3:
                print(sides + 2*" ", end="")
                x -= 3
            elif x%4 == 2:
                print(2*" ", end="")
                x -= 2
            elif x%4 == 1:
                print(" ", end="")
                x -= 1
            while x >= 4:
                print(2*sides + 2*" ", end="")
                x -= 4
            print()
        time.sleep(speed)

#NatBong 231215