class Node:
    adj = []
    def __init__(self, value, adj: list = []) -> None:
        self.value = value
        self.adj += adj

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'<Node ({self.value})>'

def dfs(node: Node):
    stack = [node]
    nodes = [node]
    while stack:
        node = stack.pop()
        for i in node.adj:
            if not i in nodes:
                stack.append(i)
                nodes.append(i)
    return nodes

def bfs(node: Node):
    queue = [node]
    nodes = [node]
    while queue:
        node = queue.pop(0)
        for i in node.adj:
            if not i in nodes:
                queue.append(i)
                nodes.append(i)
    return nodes

if __name__ == "__main__":
    nodes = [Node(i) for i in range(6)]
    nodes[0].adj = [nodes[1], nodes[2], nodes[5]]
    nodes[1].adj = [nodes[0], nodes[2], nodes[3]]
    nodes[2].adj = [nodes[0], nodes[1], nodes[4]]
    nodes[3].adj = [nodes[1], nodes[4]]
    nodes[4].adj = [nodes[3], nodes[2]]
    nodes[5].adj = [nodes[0]]
    print(dfs(nodes[3]))
    print(bfs(nodes[3]))

'''
          1 --- 3 --- 4
        /            /
5 ---- 0            /
      /            /
     2 -----------
'''

