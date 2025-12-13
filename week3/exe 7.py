class Library:
    def __init__(self):
        self.book = []
    def add_book(self,newbook):
        self.book.append(newbook)
        print('new book added')

    def show_book(self):
        for b in self.book:
            print(b)

lib = Library()
lib.add_book("book")
lib.add_book("book 2")

lib.show_book()