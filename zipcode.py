from banner import banner

banner ("ZIP CODE SORTER", "Brad")
print("Welcome to the Newaygo County zip code sorter.")

go_again = True
while go_again:


    zipcode = int(input("Please enater a zip code: "))

    if zipcode == 49309:
        print("The zipcode 49309 is for Bitely.")
    elif zipcode == 49312:
        print("The zipcode 49312 is for Brohman.")
    elif zipcode == 49337:
        print("The zipcode 49337 is for Croton and Newaygo.")
    elif zipcode == 49412:
        print("The zipcode 49412 is for Fremont.")
    elif zipcode == 49413:
        print("The zipcode 49413 is for Fremont.")
    elif zipcode == 49327:
        print("The zipcode 49327 is for Grant.")
    elif zipcode == 49349:
        print("The zipcode 49349 is for White Cloud.")
    else:
        print("The zipcode is not in Newaygo County")

    go_again = False
    if input("Would you like to enter another zipcode (Y/N)?") == "Y":
        go_again = True



print("Thank you for using the Newaygo County zip code sorter. Goodbye.")