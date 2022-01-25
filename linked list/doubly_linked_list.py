class Node:
    def __init__(self, value: int, prev=None, next=None) -> None:
        self.value: int = value # 데이터
        self.prev: Node = prev   # 이전 노드를 참조한다.
        self.next: Node = next   # 다음 노드를 참조한다.

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'<Node ({self.value})>'

class DoublyLinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head
    
    def __iter__(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp)
            temp = temp.next
        return iter(nodes)

    def __str__(self) -> str:
        return str([i.value for i in self])

    def __len__(self) -> int:
        return len(list(self.__iter__()))

    def get(self, n: int) -> Node:
        ''' n번째 노드를 반환한다. '''
        try:
            return list(self.__iter__())[n - 1]
        except IndexError:
            raise IndexError(f'{n - 1}번째 노드는 존재하지 않습니다.')

    def insert(self, node: Node, n: int) -> Node:
        ''' n번째 위치에 새로운 노드를 삽입한다. 새롭게 삽입된 노드를 반환한다. '''
        if n == 1:
            self.head, node.prev, node.next = node, None, self.head
            return node
            
        left = self.get(n - 1)
        node.prev, node.next = left, left.next
        if left.next:
            left.next.prev = node
        left.next = node
            
        return node

    def delete(self, n: int) -> Node:
        ''' n번째 노드를 삭제한다. 삭제된 노드를 반환한다. '''
        if n == 1:
            target = self.head
            self.head, target.next.prev = target.next, None
            return target

        left = self.get(n - 1)
        target = left.next
        left.next, target.next.prev = target.next, left
        return target

if __name__ == "__main__":
    ll = DoublyLinkedList(Node(1))
    for i in range(2, 6):
        ll.insert(Node(i), i)
    print(ll)
    print(ll.get(3))
    ll.insert(Node(10), 3)
    print(ll)
    print(ll.get(4).prev)
    print(ll.get(3).prev, ll.get(3).next)
    ll.delete(3)
    print(ll)
    print(ll.get(2).next, ll.get(3).prev)

