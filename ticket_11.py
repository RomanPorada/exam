from abc import ABC, abstractmethod

result_list = [x**2 if x % 2 == 0 else -1 for x in range(1, 11, 2)]

print(result_list)

# Правильна відповідь [-1, -1, -1, -1, -1]

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(number)

while True:
    try:
        numeric = int(input("Введіть число:"))
        break
    except ValueError:
        print("Потрібно вводити число")

fizzbuzz(numeric)


def decorator(func):
    def wraper(*args, **kvargs):
        wraper.challenge += 1
        print(f"Функція {func.__name__} викликана {wraper.challenge} разів")
        return func(*args, **kvargs)
    wraper.challenge = 0
    return wraper
    

@decorator
def add(a, b):
    print(a+b)

add(1, 5)
add(3, 1)
add(6, 4)

class Animal(ABC):
    @abstractmethod
    def hibernate(self):
        return None

class Bear(Animal):
    def hibernate(self):
        print("Ведмідь впадає в сплячку")

class Sheep(Animal):
    def hibernate(self):
        raise ValueError("Вівця не впадає в сплячку")
    
def main():
    Vinipuh = Bear()
    Shon = Sheep()
    Lox = Bear()
    animals = [Vinipuh, Shon, Lox]
    for animal in animals:
        try:
            animal.hibernate()
        except ValueError as e:
            print(f"Неможлива дія: {e}")

if __name__  == "__main__":
    main()