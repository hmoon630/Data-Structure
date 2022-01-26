# 그래프 (Graph)

## 기본 개념
그래프는 vertex와 edge로 구성된 자료구조 이다. vertex는 정점, edge는 정점과 정점을 연결하는 간선이다.

![그래프 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Directed.svg/220px-Directed.svg.png)

### 그래프 용어 
- 정점(vertex): 노드(Node)라고도 하며, 정점에 데이터가 저장 된다.
- 간선(edge): 노드 간의 관계를 나타낸다.
- 인접 정점(adjacent vertex): 간선에 의해 직접 연결되어 있는 정점
- 차수(degree): 무방향 그래프에서 한 정점에 인접한 정점의 수
- 진입 차수(in-degree): 방향 그래프에서 외부에서 오는 간선의 수
- 진출 차수(out-degree): 방향 그래프에서 외부로 가는 간선의 수
- 단순 경로(simple path): 반복되는 정점이 없는 경로
- 사이클(cycle): 단순 경로에서 시작 정점과 종료 정점이 동일한 경로

## 그래프의 탐색
일반적으로 DFS(깊이 우선 탐색, Depth-First Search)와 BFS(너비 우선 탐색, Breadth-First Search) 두 가지 방법을 주로 사용한다.

### DFS
한 노드에서 시작하여 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법이다. -

- 모든 노드를 방문하고자 할 때 이 방법을 선택한다.

### BFS
한 노드에서 시작하여 인접한 노드를 먼저 탐색하는 방법

- 두 노드 사이에 최단 경로, 혹은 임의의 경로를 찾고자 할 때 선택한다.

## References
[[자료구조] 그래프(Graph)란 by heejeong Kwon](https://gmlwjd9405.github.io/2018/08/13/data-structure-graph.html)