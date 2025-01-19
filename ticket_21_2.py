from abc import ABC, abstractmethod

students = {"Student_1": 75, "Student_5": 92, "Student_2": 88, "Student_12": 78, "Student_8": 96}

failed_students = dict(filter(lambda item: item[1] < 80, students.items()))
print(failed_students)
# Правильна відповідь: {'Student_1': 75, 'Student_12': 78}

def leters(str):
    new_string = ''
    for leter in str:
        if leter.islower():
            new_let = leter.upper()
        else:
            new_let = leter.lower()
        new_string += new_let
    print(new_string)

str = "SJKYUhjguy"
leters(str)

def decorator(func):
    def wrapper(*args):
        result = func(*args)
        if result > 0:
            return result
        else:
            return None
    
    return wrapper

@decorator
def fnc(val1, val2):
    return val1 + val2

print(fnc(3, 4))

class Fruit(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def eat(self):
        pass

class Apple(Fruit):

    def eat(self):
        print(F"Смачного! Яблуко {self.name}")

class Orange(Fruit):

    def eat(self):
        print(F"Смачного! Апельсин {self.name}")

class ToxicApple(Apple):
    def eat(self):
        raise ToxicAppleExeption("Це яблуко отруйне його не слід їсти")
    
class ToxicAppleExeption(Exception):
    """Це яблуко отруйне його не слід їсти"""
    pass

def main():
    apple_1 = Apple("a")
    apple_2 = Apple("b")
    orange_1 = Orange("c")
    toxic_aplle = ToxicApple("t")
    fruits = [apple_1, orange_1, toxic_aplle, apple_2]
    for fruit in fruits:
        try:
            fruit.eat()
        except ToxicAppleExeption as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
