# 스택 (Stack)

## 기본 개념
스택(Stack)은 한쪽 끝에서만 자료를 넣고 뺄 수있는 LIFO(Last-In-First-Out) 자료구조이다.

자료를 넣는 것을 Push라고 부르고, 자료를 빼는 것을 Pop이라고 부른다. 이때 나오는 자료는 가장 마지막으로 Push한 자료이다.
![스택 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/1280px-Data_stack.svg.png)

스택은 주로 4가지의 연산을 수행한다.
- top: 스택의 가장 위에 있는 데이터를 반환한다.
- pop: 스택의 가장 위에 있는 데이터를 삭제한다.
- push: 스택의 가장 위에 메모리를 생성하고 데이터를 넣는다.
- empty: 스택이 비어있으면 1, 그렇지 않으면 0을 반환한다.
