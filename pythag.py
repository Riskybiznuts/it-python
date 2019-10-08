from math import sqrt
print("Input lengths of shorter triangle sides:")


go_again = True
while go_again:

    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    if a == "":
        b = float(b)
        c = float(c)
        a = sqrt(c*c-b*b)
        print(f"your missing side is a and it's length is {a}")
    elif b == "":
        c = float(c)
        a = float(a)
        b = sqrt(c*c-a*a)
        print(f"your missing side is b and it's length is {b}")
    elif c == "":
        a = float(a)
        b = float(b)
        c = sqrt(a*a+b*b)
        print(f"your missing side is c and it's length is {c}")

    go_again = False
    if input("would you like to calculate another triangle (Y/N)?") == "Y":
        go_again = True
print("Thank you for using the Pythagorean Calculator.")





