import journal
from banner import banner

banner("DEEP THOUGHTS" , "URGOD")

def main():
    run_event_loop main():

def run_event_loop():
    filename = "default"
    journal_data = journal.load(filename)#[]

    while True:
        command = input("[L]ist entries, [A]dd an entry, E[x]it: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() == "X":
            break
        else:
            print("You Idiot! There are only three options and you tried to choose a fourth")
    journal.save(filename, journal_data)


def list_entries(data):
    print("Your journal entries")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")





def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    #data.append(entry)









main()