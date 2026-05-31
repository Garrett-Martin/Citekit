#ideal format:
# [Tag]
# Alexander Thomas Macdonald 23, 8-16-2023,
# [First Middle Last] [last two digits of year], [full date],
# [qualifications]. [Title], [Publication], [URL], [Signature]
# **The Tag, last name, and the last two digits of the year are bolded



def author_formatting(author):
    author_list = author.split(" & ")
    ev_author = ""
    if len(author_list) == 1:
        ev_author = author_list[0].split()[-1]

    elif len(author_list) == 2:
        last1 = author_list[0].split()[-1]
        last2 = author_list[1].split()[-1]

        ev_author = f"{last1} & {last2}"

    else:
        ev_author = author_list[0].split()[-1] + " et al"

    return ev_author



def format_citation(source):

    tag = source["tag"]
    author = source["author"]
    qualifications = source["qualifications"]
    title = source["title"]
    publication = source["publication"]
    date = source["date"]
    url = source["url"]
    signature = source["signature"]


    ev_author = author_formatting(author)
    short_year = date[-2:]           #gets the two digit date

    citation = (
    #not a tuple, uses f strings to insert the input and
    #glues them together with the parentheses at the ends
        f"[{tag}]\n"
        f"{ev_author} {short_year} — "
        f"{author}, "
        f"{qualifications}. "
        f"\"{title},\" "  #for quotations
        f"{publication}, " #look into process for italicizing in terminal
        f"{date}, "
        f"{url}, "
        f"{signature}"
    )

    return citation
    