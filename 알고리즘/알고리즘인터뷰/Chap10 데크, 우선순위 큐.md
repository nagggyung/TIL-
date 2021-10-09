### Chap10 데크, 우선순위 큐

### 데크(Deque):
- 데크(Deque)는 더블 엔디드 큐(Double-Ended Queue)의 줄임말로, 글자 그대로 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)이다.
- 데크는 양쪽에서 삭제와 삽입을 모두 처리할 수 있으며, 스택과 큐의 특징을 모두 갖고 있다.
- 파이썬은 데크 자료형을 다음과 같이 collections 모듈에서 deque라는 이름으로 지원한다.

![2021-10-10](https://user-images.githubusercontent.com/74478432/136664251-81caca15-24b3-45db-a041-0e2615613c36.png)


### 문26) 원형 데크 디자인(리트코드 641. Design Circular Deque)

### Solution (1) 이중 연결 리스트를 이용한 데크 구현

```c 
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        
    # 이중 연결 리스트에 신규 노드 삽입    
    def _add(self, node:ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    
    def _del(self, node:ListNode):
        n = node.right.right
        node.right = n
        n.left = node
        
    def insertFront(self, value: int) -> bool:
        if self.len == self.k :
            return False
        self.len+=1
        self._add(self.head, ListNode(value))
        return True 
        
    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
        
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
        
    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


```



