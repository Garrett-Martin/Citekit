import json


#everything that touches evidence.json


#---------------load/save refactored to avoid repeat code--------------
def load_evidence():
    try:
        with open("evidence.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    

def save_evidence(sources):
    with open("evidence.json", "w") as file:
        json.dump(sources, file, indent=4)
#-----------------------------------------------------------------------




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

    sources = load_evidence()
    sources.append(new_source)
    save_evidence(sources)
    print("\nSource added to evidence.json\n")







#UI purposes
def display_evidence(source):
    print("-----------------------------------------------------------------")

    print(f"Author: {source['author']}")
    print(f"Title: {source['title']}")
    print(f"Publication: {source['publication']}")
    print(f"Date: {source['date']}")
    print(f"URL: {source['url']}")
    print(f"Tag: {source['tag']}")
    print(f"Notes: {source['notes']}")
    
    print("------------------------------------------------------------------")
    print()


def view_sources():
    sources = load_evidence()

    if len(sources) == 0:
        print("\nNo saved evidence.\n")
        return
    
    for source in sources:
        display_evidence(source)







def search_evidence():
    keyword = input("Enter keyword: ").lower() #takes user input and lowercases it

    found = False

    sources = load_evidence() #part of new refactored code

    for source in sources: #loops through each dictionary
        for value in source.values(): #loops through each field in dictionary
            if keyword in str(value).lower(): #lower() only works on strings
                print(source)
                print()
                break

    if not found:
        print("\nNo matching evidence found.\n")



def filter_by_tag():
    keyword = input("Enter tag: ").lower()

    sources = load_evidence()

    found = False
    for source in sources:
        tag = source.get("tag", "").lower()

        if keyword in tag:
            display_evidence(source)
            found = True

    if not found:
        print("\nNo matching tags found.\n")


def filter_by_author():
    keyword = input("Enter author: ").lower()

    sources = load_evidence()

    found = False
    for source in sources:
        author = source.get("author", "").lower()

        if keyword in author:
            display_evidence(source)
            found = True

    if not found:
        print("\nNo matching authors found.\n")