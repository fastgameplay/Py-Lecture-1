class Book:
    def __init__(self, title, author, publisher):
        self._title = title
        self._author = author
        self._publisher = publisher
#მიყვარს პიტონის ინკაპსულაცია <3
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    def __str__(self):
        return f"{self._title}, {self._author}, {self._publisher}"


book = Book("Initial Title", "Initial Autor", "Initial Publisher")
print(str(book))
# Output: "Initial Title, Initial Autor, Initial Publisher"

book.title = "New Title"
book.author = "New Author"
book.publisher = "New Publisher"
print(str(book))
# Output: "New Title, New Author, New Publisher"