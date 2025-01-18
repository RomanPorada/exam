result_dict = {f"{x}-value": x ** 2 if x ** 2 % 2 != 0 else -1 for x in range(1, 6)}

print(result_dict)
# Правильна відповідь: {'1-value': 1, '2-value': -1, '3-value': 9, '4-value': -1, '5-value': 25}

def average(*args):
    number = 0
    sum = 0
    for i in args:
        if type(i) == int:
            sum += i
            number += 1
    
    return sum/number
    
result = average(2, 4, 4.3, 3, 6.4)
print(result)

def decorator(func):
    def wrapper():
        print(f"Function {func.__name__} has been executed")
        return func()
    return wrapper

@decorator
def text():
    print("I am Betmen")

text()

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Стек порожній ви не можете видалити з нього елемент")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Стек порожній нема на що дивитися")

    def isEmpty(self):
        return len(self.items) == 0
    
stack = Stack()
stack.push(12)
stack.push(17)
print(stack.peek())
stack.push(18)
print(stack.peek())
stack.pop()
print(stack.isEmpty())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.isEmpty())
