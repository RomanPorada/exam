from abc import ABC, abstractmethod

class BookReservation(ABC):
    @abstractmethod
    def reserveBook(self, bookId: str):
        pass

class Library(BookReservation):
    def __init__(self):
        self.reserved_books = []  
        self.books_map = { 
            "odi_1": Book("odi_1", "Одіссея"),
            "lip_1": Book("lip_1", "Маленький принц"),
            "mat_1": Book("mat_1", "Математика")
        }

    def reserveBook(self, bookId: str):
        if bookId in self.reserved_books:
            raise BookUnavailableException(f"Книга з ID {bookId} вже зарезервована.")
        if bookId not in self.books_map:
            raise BookUnavailableException(f"Книга з ID {bookId} недоступна для резервування.")

        self.reserved_books.append(bookId)
        self.books_map.pop(bookId)

class Book():
    bookId: str
    title: str

    def __init__(self, bookId, title):
        self.bookId = bookId
        self.title = title

class BookUnavailableException(Exception):
    pass

if __name__ == "__main__":
    library = Library()

    try:
        library.reserveBook("odi_1")
        print("Книга 'Одіссея' зарезервована.")
        
        library.reserveBook("odi_1")
    except BookUnavailableException as e:
        print(e)

    try:
        library.reserveBook("non_existent")
    except BookUnavailableException as e:
        print(e)

def ansver(lst: list):
    lenght =  lst.__len__()
    sum = 0
    for el in lst:
        sum += el
    return sum / lenght

print(ansver([5, 4, 5]))

class Set():
    def __init__(self, elements=None):
        self.elements = list(elements) if elements else []
    
    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        
    def contains(self, elemet):
        return elemet in self.elements
    
    def size(self):
        return self.elements.__len__()
    
    def __str__(self):
        return f"{self.elements}"

def main():        
    set = Set([3, 5])  
    print(set)     
    set.insert(1)
    print(set)
    print(set.size())
    set.remove(3)
    print(set)
    print(set.contains(2))
    print(set.contains(5))

if __name__ == "__main__":
    main()
