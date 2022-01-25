class Queue:    
    items = []

    def __init__(self) -> None:
        pass
    
    def enqueue(self, item):
        self.items.append(item)
        return item
    
    def dequeue(self):
        return self.items.pop(0)

if __name__ == "__main__":
    q = Queue()

    for i in range(3):
        q.enqueue(i)
    
    print(q.dequeue())
    q.enqueue(5)
    
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())