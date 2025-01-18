original_str = "Hello"

result_list = "".join([sum * 2 for sum in original_str][::-1])

print(result_list)

# Правильна відповідь: oolllleeHH

new_list = []

def func(*args):
    for i in args:
        if i % 2 == 0:
            i = i ** 3
            new_list.append(i)
        else:
            new_list.append(i)

while True:
    numeric = input("Введіть числа через кому: ")
    try:
        numeric_list = list(map(int, numeric.split(",")))
        break
    except ValueError:
        print("Потрібно вводити лише числа")

func(*numeric_list)
print(new_list)

def decorator(func):
    def wrapper(*args):
        print(f"Function has been executed with the following parameters - {args}")
        return func(*args)
    return wrapper

numeric_sum = 0

@decorator
def sum(*args):
    global numeric_sum
    for i in args:
        numeric_sum += i

sum(1, 4, 5, 3, 6)

class Set():
    def __init__(self, elements=None):
        self.elements = list(elements) if elements else []
    
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        
    def contains(self, elemet):
        return elemet in self.elements
    
    def __str__(self):
        return f"{self.elements}"
            
set = Set([3, 5])  
print(set)     
set.add(1)
print(set)
set.remove(3)
print(set)
print(set.contains(2))
print(set.contains(5))