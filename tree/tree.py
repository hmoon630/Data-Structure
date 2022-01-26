class Node:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value: int = value  # 데이터
        self.left: Node = left  # 왼쪽의 자식 노드를 참조한다.
        self.right: Node = right  # 오른쪽의 자식 노드를 참조한다.

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"<Node ({self.value})>"

def in_order(node: Node):
    if node is not None:
        in_order(node.left)
        print(node.value, end=" ")
        in_order(node.right)

def pre_order(node: Node):
    if node is not None:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)

def post_order(node: Node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=" ")

if __name__ == "__main__":
    # README.md 파일의 이미지를 트리로 구현
    tree = Node(
        left=Node(
            left=Node(2), value=7, right=Node(left=Node(5), value=6, right=Node(11))
        ),
        value=2,
        right=Node(value=5, right=(Node(left=Node(4), value=9))),
    )

    print("---- in-order ----")
    in_order(tree)
    print()

    print("---- pre-order ----")
    pre_order(tree)
    print()
    
    print("---- post-order ----")
    post_order(tree)
    print()
