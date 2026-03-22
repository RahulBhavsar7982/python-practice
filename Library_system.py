import json

class Book:             
    def __init__(self, title, author):
        self.title     = title
        self.author    = author
        self.available = True

    def borrow(self):
        if self.available == False:
            print(f" {self.title} already borrowed!")
        else:
            self.available = False
            print(f" Borrowed: {self.title}")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned!")


class Library:
    def __init__(self):
        self.books=[]

    

    def add_books(self,book):
        self.books.append(book)
        print(f"\n{book.title} Added Sucesfully")

    def show_all(self):
        for i,book  in enumerate(self.books,1):
            status= "Yes " if book.available else "No"
            print(f" \n {i}. {book.title} - {book.author} -  Available:{status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
               book.borrow()
            return       
        print(" Book not found!")
            
    def save(self):
        data=[]
        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author,
                "available": book.available
            })
        with open("library.json" ,"w") as f:
            json.dump(data,f)

library = Library()

b1 = Book("Python Crash Course", "Eric Matthes")
b2 = Book("Atomic Habits", "James Clear")
b3 = Book("Deep Learning", "Ian Goodfellow")

library.add_books(b1)
library.add_books(b2)
library.add_books(b3)

library.borrow_book("Python Crash Course")
library.borrow_book("Python Crash Course")

library.show_all()
library.save()

    

