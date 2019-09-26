import os
from banner import banner
banner("HTML TAG COUNTER" , "Brad")

print("Welcome to the HTML tag counter")

def load(filename):
    data = []
    print(f"..... loading from {filename}")

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def count_tags(text):
    count = 0
    previous_char = None
    for char in text:
        if char != "/" and previous_char == "<":
            count = count + 1
        previous_char = char
    return count



go_again = True
while go_again:
    name = input("Please enter the name of the HTML file:")
    data = load(name)
    tagcount = 0
    for line in data:
        tagcount = tagcount + count_tags(line)
    print(tagcount)
    if input("Would you like to count another html file (Y/N)?") != "Y":
        go_again = False


print("Thank you for using the HTML tag counter")



