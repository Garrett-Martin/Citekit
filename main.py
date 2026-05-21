import json

def start_menu():

    print("Welcome to Citekit")

    print("1.  Add source manually")
    print("2.  Scrape source from URL")
    print("3.  View saved sources")
    print("4.  Search sources")
    print("5.  Export citation")
    print("6.  Quit")

    while True:
        choice = input("Enter option: ")

        if choice == "1":
            add_source()
        elif choice == "2":
            pass
        elif choice == "3":
            opens_source()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            exiting = "Program in exiting"
            print(exiting)
            return False
        else:
            print("Invalid option, enter 1-6.")


sources = []

def add_source():
    author = input("author: ")
    title = input("title: ")
    publication = input("publication: ")
    date = input("date: ")
    url = input("url: ")
    tag = input("tag: ")
    notes = input("notes: ")

    new_source = {
        "author": author,
        "title": title,
        "publication": publication,
        "date": date,
        "url": url,
        "tag": tag,
        "notes": notes
    }

    try:
        with open("evidence.json", "r") as file:
            sources = json.load(file)
    except FileNotFoundError:
        sources = []

    sources.append(new_source)

    with open("evidence.json", "w") as file:
        json.dump(sources, file, indent=4)
    print("Source added to evidence.json")




def opens_source():
    with open("evidence.json", "r") as file:
        sources = json.load(file)
        for source in sources:
            print(source)


def main():
    start_menu()


main()