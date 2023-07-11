class Library:
  def __init__(libr):
    libr.noBooks = 0
    libr.books = []
    
  def addBook(libr,book):
   libr.books.append(book)
   libr.noBooks = len(libr.books) # counting books

  def showInfo(libr):
    print(f"There are {libr.noBooks} books in the Library")
    for book in libr.books:
      print(book)

l1 = Library()
l1.addBook("All or Nothing")
l1.addBook("Persuader")
l1.showInfo()