class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added to library")

    def show_books(self):
        print("Available Books:")
        for book in self.books:
            print("-", book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued")
        else:
            print(f"{book} not available")

    def return_book(self, book):
        self.books.append(book)
        print(f"{book} returned")


# Create object
lib = Library()

# Operations
lib.add_book("Python")
lib.add_book("Java")
lib.add_book("Cyber Security")

lib.show_books()

lib.issue_book("Python")
lib.show_books()

lib.return_book("Python")
lib.show_books()
