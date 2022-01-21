# 연결 리스트 (Linked list)

## 기본 개념

![연결 리스트 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/816px-Singly-linked-list.svg.png)

연결 리스트의 각각 객체는 주로 노드(Node)라고 부른다.

노드에서 다음 노드의 주소를 가진 필드를 포인터(Pointer)라고 부른다. 그리고 정보를 담고 있는 필드를 데이터(Data)라고 부른다.

리스트에서 첫 번째 노드는 헤드(Head), 마지막 노드는 테일(Tail)이라고 부른다.

### **단일 연결 리스트 (Singly linked list)**

단일 연결 리스트는 노드에 데이터와 하나의 포인터로 이루어져 있다. 포인터는 다음 노드를 가리키고 있다.

테일의 다음 포인터는 비어있는 값(Null)을 참조한다.

### **이중 연결 리스트 (Doubly linked list)**

![이중 연결 리스트 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

이중 연결 리스트는 노드에 데이터와 두개의 포인터로 이루어져 있다. 포인터는 각각 이전 노드와 다음 노드를 가리키고 있다.
헤드의 이전 포인터와 테일의 다음 포인터는 비어있는 값(Null)을 참조한다.

### **순환 연결 리스트 (Circular linked list)**

![순환 연결 리스트 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/350px-Circularly-linked-list.svg.png)

연결 리스트는 주로 테일이 Null을 참조하게 된다. 대신 순환 연결 리스트의 테일의 포인터는 헤드를 참조하여 순환(Circular)하게 된다. 반면에 순환하지 않으면 선형(Linear) 리스트 된다.

이중 순환 연결 리스트의 경우는 헤드의 포인터가 테일을 참조하게 된다.

## 시간 복잡도

| 행위              | 시간 |
| ----------------- | ---- |
| n번째 데이터 읽기 | O(n) |
| 삽입              | O(1) |
| 삭제              | O(1) |
| n번째 노드에 삽입 | O(n) |
| n번째 노드 삭제   | O(n) |

### 읽기

연결 리스트의 n번째 요소의 값을 읽기 위해서는 헤드부터 차례대로 포인터를 따라 접근해야 하기 때문에 O(n)의 시간이 소요된다.

### 삽입

A 노드와 B 노드 사이에 N 노드를 삽입 한다고 가정한다.

N 노드의 포인터는 B 노드를 참조하고, A 노드의 포인터는 N 노드를 참조하도록 한다.
따라서 O(1)의 시간이 소요된다.

하지만 n번째 노드와 n + 1번째 노드에 삽입하게 될 경우, 헤드부터 차례대로 접근해야 하기 떄문에 O(n)의 시간이 걸리게 된다.

### 삭제

A 노드와 C 노드 사이에 있는 B 노드를 삭제 한다고 가정한다.

A 노드의 포인터를 B 노드의 포인터(C 노드를 참조하고 있다.)를 참조하도록 하고, B 노드를 지운다.
따라서 O(1)의 시간이 소요된다.

하지만 n번째 노드를 지우게 될 경우, 헤드부터 차례대로 접근해야 하기 때문에 O(n)의 시간이 걸리게 된다.
