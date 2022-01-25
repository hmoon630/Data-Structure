from ctypes import pointer


class Stack:
    items = []
    pointer = -1

    def __init__(self) -> None:
        pass

    def top(self):
        return self.items[self.pointer]

    def pop(self):
        item = self.items.pop(self.pointer)
        self.pointer -= 1
        return item

    def push(self, item):
        self.pointer += 1
        self.items.append(item)
        return item
    
    def empty(self):
        return False if self.pointer else True

if __name__ == "__main__":
    s = Stack()
    for i in range(3):
        s.push(i)
    print(s.top())
    print(s.pop())
    print(s.top())
    print(s.empty())
    
    print(s.push(7))

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.empty())