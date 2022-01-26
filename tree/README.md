# 트리 (Tree)

## 기본 개념
트리란 그래프의 일종으로, 여러 노드가 한 노드를 가리키지 않는 구조이다.
또한 서로 다른 두 노드를 잇는 길이 하나뿐인 그래프를 트리라고 부른다.

트리에서 최상위 노드는 루트 노드(root node)라고 한다. 노드 A가 노드 B를 가리킬 때, A는 B의 부모 노드, B는 A의 자식 노드가 된다. 또한 자식 노드가 없는 노드는 잎 노드(leaf node)라고 한다.

## 이진 트리 (Binary tree)
이진 트리는 각각의 노드가 최대 2개의 자식 노드를 가지는 트리 구조이다. 

![이진 트리 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/1024px-Binary_tree.svg.png)

### 이진 트리의 탐색
다음의 방법들이 주로 사용된다.

- in-order(중위 순회): 왼쪽 자식노드(L), 내 노드(P), 오른쪽 자식노드(R) 순서로 방문한다.
- pre-order(전위 순회): 내 노드(P), 왼쪽 자식노드(L), 오른쪽 자식노드(R) 순서로 방문한다.
- post-order(후위 순회): 왼쪽 자식노드(L), 오른쪽 자식노드(R), 내 노드(P) 순서로 방문한다.
- level-order(레벨 순회): 내 노드(P), 내 노드로부터 깊이 1인 노드들, 내 노드로부터 깊이 2인 노드들, ... , 내 노드로부터 깊이 N인 노드들 순서로 방문한다.

## B-트리(B-tree)
B-트리는 데이터베이스와 파일 시스템에서 주로 사용되는 트리 구조이다. 이진 트리에서 확장하여 2개 이상의 자식 노드를 가질 수 있다.

![B-트리 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/B-tree.svg/400px-B-tree.svg.png)