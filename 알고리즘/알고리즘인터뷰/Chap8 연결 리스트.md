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





