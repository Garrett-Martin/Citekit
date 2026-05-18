import json

print("Welcome to Citekit")

print("1.  Add source manually")
print("2.  Scrape source from URL")
print("3.  View saved sources")
print("4.  Search sources")
print("5.  Export citation")
print("6.  Quit")



def create_source():
    
    author = input("author: ")
    title = input("title: ")
    publication = input("publication: ")
    date = input("date: ")
    url = input("url: ")
    tag = input("tag: ")
    notes = input("notes: ")

    source = {
        "author": author,
        "title": title,
        "publication": publication,
        "date": date,
        "url": url,
        "tag": tag,
        "notes": notes
    }

    return source

def save_source(source):
    with open("source.json", "w") as file:
        json.dump(source, file, indent=4)



def main():
    source = create_source()
    save_source(source)
    print("Source saved to source.json")


main()