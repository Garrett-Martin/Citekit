import requests
from bs4 import BeautifulSoup


def scrape_source(url):

    #Wrap the entire scraper in a try/except block
    try:
        #send HTTP GET request
        response = requests.get(url)

        #Takes raw HTML from response and parse it into BS object
        soup = BeautifulSoup(response.text, "html.parser")

        # 1 ---------------------------------
        #Find first meta tag with:
        #property="og:title"
        title = soup.find(
            "meta",
            property="og:title"
        )["content"]

        # 2 ---------------------------------
        publication = soup.find(
            "meta",
            property="og:site_name"
        )["content"]

        #Split timestamp string at the T:
        #ex: "2023-08-16T12:45:00Z"
        #[0] gets first piece before T
        raw_date = soup.find("meta", property="article:published_time")["content"]
        date = raw_date.split("T")[0]

        # 3 ---------------------------------
        #find_all() returns a LIST
        author_tags = soup.find_all(
            "meta",
            property="article:author"
        )

        authors = []

        for author in author_tags:
            authors.append(author["content"])

        #join the pieces together
        author_string = " & ".join(authors)


        # DICTIONARY CREATION -----------------
        #build final source dictionary using extracted data
        source = {
            "author": author_string,
            "title": title,
            "publication": publication,
            "date": date,
            "url": url,
            "tag": "",                  #empty string = cannot infer reliably
            "notes": "",
            "qualifications": "",
            "signature": ""
        }
#ask for manual entry for tag, notes, quals, signature


        return source
    
    except Exception as error:
        print("Scraping failed.")
        print(error)
        return None
