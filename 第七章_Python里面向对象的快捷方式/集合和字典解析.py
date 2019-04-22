from  collections import namedtuple

Book = namedtuple("Book", "author title genre")

books =[
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief of time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A wizard of earth", "fantasy")
]

fantasy_authors = {
    b.author for b in books if b.genre == "fantasy"
}
print(fantasy_authors)