class Book:

    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Number of Pages: {self.pages}"
    def __len__(self):
        return self.pages


myBook = Book("Python Rocks!","Faiz",359)
print(myBook)
length_book = len(myBook)
print(length_book)
