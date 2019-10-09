from banner import banner
from math import sqrt
banner("PYTHAGOREAN CALCULATOR" , "By BRAD")
print("We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print("")


go_again = True
while go_again:
    print("Please enter the length of each side, or leave it blank if you don't know.")
    print("")
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



