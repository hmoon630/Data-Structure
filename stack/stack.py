from operator import itemgetter
from typing import ItemsView


class Stack:
    items = []
    
    def __init__(self) -> None:
        pass

    def top(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop(-1)

    def push(self, item):
        self.items.append(item)
        return item
    
    def empty(self):
        return False if len(self.items) else True

if __name__ == "__main__":
    s = Stack()
    for i in range(3):
        s.push(i)
    print(s.top())
    print(s.pop())
    print(s.top())
    print(s.empty())
    
    print(s.push(7))
    print(s.top())

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.empty())