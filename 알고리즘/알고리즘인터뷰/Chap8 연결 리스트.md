### 연결리스트
* 연결리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지는 않는다. 
* 연결리스트는 배열과는 달리 특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. 즉, 탐색에는 O(n)이 소요된다. 반면, 시작 또는 끝 지점에 아이템을 
  추가하거나 삭제, 추출하는 작업은 O(1)에 가능하다. 

### 문13) 펠린드롬 연결리스트(리트코드 234. Palindrome Linked List)

### Solution)

```c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s: Deque = collections.deque()
        if not head:
            return True 
        node = head
        
        while node is not None:
            s.append(node.val)
            node = node.next
        while len(s)>1:
            if s.pop() != s.popleft():
                return False
        
        return True 
```

파이썬의 데크(Deque)는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도 O(1)에 실행된다.

### 런너 기법:
런너(Runner)는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수
있다. 2개의 포인터는 각각 빠른 런너(Fast Runner), 느린 런너(Slow Runner)라고 부르는데, 대게 빠른 런너(포인터)는 두 칸씩 건너 뛰고 느린 런너(포인터)는 한 칸씩 이동하게 된다. 

빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결리스트의 *중간 지점*을 가리키게 된다. 이 같은 방식으로 중간 위치를 찾아 내면, 여기서 부터 값을 비교하거나 뒤집기를 
시도하는 등 여러모로 활용할 수 있어 연결 리스트 문제에서는 반드시 쓰이는 기법이다. 

### 런너기법 Solution)


```c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
        
```

### 문14) 두 정렬 리스트의 병합 (리트코드 21. Merge Two Sorted Lists)

### Solution)

```c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
        
```


### 문15) 역순 연결 리스트(206. Reverse Linked List)

### Solution)


```c
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
        
```
* node.next 를 prev 리스트로 계속 연결하면서 끝날 때 까지 반복
* node 가 None이 될 때, prev는 뒤집힌 연결 리스트의 첫 번째 노드가 된다. 

### 문16) 두 수의 덧셈(리트코드 2. Add Two Numbers)

### Solution (1) 자료형 반환)

```c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
        
    # 연결 리스트 뒤집기
    def reversedList(self, head:ListNode) -> List:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node:ListNode) -> List:
        list:List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    # 파이썬 리스트의 연결리스트로의 변환
    def toReversedLinkedList(self, result: str)->ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode)->ListNode:
        a = self.toList(self.reversedList(l1))
        b = self.toList(self.reversedList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        # 최종 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))
        
```


### Solution (2) 전가산기 구현)


```c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력 값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next
        
```

* 입력 값 A와 B, 이전의 자리 올림수(carry in) 이렇게 3가지 입력으로 합(sum)과 다음 자리 올림수(carry out) 여부를 결정
* 연산 결과로 나머지(Remainder)를 취하고 몫(Quotient)은 자리올림수 형태로 올린다.
* carry, val = divmod(sum + carry, 10): divmod()는 파이썬 내장 함수로, 몫과 나머지로 구성된 튜플을 리턴한다. 
* divmod(a,b) = (a // b, a % b)



