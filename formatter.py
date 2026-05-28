#ideal format:
# [Tag]
# Alexander Thomas Macdonald 23, 8-16-2023,
# [First Middle Last] [last two digits of year], [full date],
# [qualifications]. [Title], [Publication], [URL], [Signature]
# **The Tag, last name, and the last two digits of the year are bolded


def format_citation(source):

    tag = source["tag"]
    author = source["author"]
    qualifications = source["qualifications"]
    title = source["title"]
    publication = source["publication"]
    date = source["date"]
    url = source["url"]
    signature = source["signature"]


    last_name = author.split()[-1]   #gets last name
    short_year = date[-2:]           #gets the two digit date

    citation = (
    #not a tuple, uses f strings to insert the input and
    #glues them together with the parentheses at the ends
        f"[{source['tag']}]\n"
        f"{last_name} {short_year} — "
        f"{author}, "
        f"{qualifications}. "
        f"\"{title},\" "  #for quotations
        f"{publication}, " #look into process for italicizing in terminal
        f"{date}, "
        f"{url}, "
        f"{signature}"
    )

    return citation
    