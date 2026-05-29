import storage
import formatter
import scraper

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
            storage.add_source()
        elif choice == "2":
            url = input("Enter URL: ")
            scraped_source = scraper.scrape_source(url)
            print(scraped_source)
        elif choice == "3":
            storage.view_sources()
        elif choice == "4":
            storage.search_evidence()
        elif choice == "5":
            formatter.format_citation()
        elif choice == "6":
            exiting = "Program in exiting"
            print(exiting)
            return False
        else:
            print("Invalid option, enter 1-6.")

sources = []



def main():
    start_menu()


main()