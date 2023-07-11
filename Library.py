class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)  # counting books

  def removeBook(self, book):
    if book in self.books:
      self.books.remove(book)
      self.noBooks = len(self.books)  # updating book count
      print(f"The book '{book}' has been removed")
    else:
      print(f"The book '{book}' is not found in the library")

  def showInfo(self):
    print(f"There are {self.noBooks} books in the Library")
    for book in self.books:
      print(book)

l1 = Library()
l1.addBook(input("Add Book: "))

book_to_remove = input("Enter the book you want to remove: ")
l1.removeBook(book_to_remove)

l1.showInfo()