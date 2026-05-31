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
            if scraped_source is not None:
                print(scraped_source)

                scraped_source["qualifications"] = input("Paste in Qualifications: ")
                
                scraped_source["tag"] = input("Paste in Tag: ")

                scraped_source["notes"] = input("Paste in Notes: ")

                scraped_source["signature"] = input("Paste in Signature: ")

                sources = storage.load_evidence()
                sources.append(scraped_source)
                storage.save_evidence(sources)

                print("Scraping Successful")
            else:
                print("Scraping failed.")

        elif choice == "3":
            storage.view_sources()
        elif choice == "4":
            storage.search_evidence()
        elif choice == "5":
            sources = storage.load_evidence()

            if len(sources) == 0:
                print("\nNo saved sources.\n") #edge case

            else:
                print("\nSaved Sources:\n")

                for index, source in enumerate(sources):
                    print(
                        f"{index + 1}. "
                        f"{source['author']} : "
                        f"{source['title']}"
                    )
                pick = input("\nSelect a source number: ")
                selected = sources[int(pick) - 1]
                citation = formatter.format_citation(selected)
                print("\nFormatted Citation")
                print(citation)

            formatter.format_citation(sources)
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



