import json


#everything that touches evidence.json


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




def search_evidence():
    