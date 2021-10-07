### Chap9. 스택, 큐
- 스택은 LIFO(Last-In-First-Out, 후입선출), 큐는 FIFO(First-In-First-Out, 선입선출)로 처리된다.
- 파이썬은 스택 자료형을 별도로 제공하지는 않지만, 리스트가 사실상 스택의 모든 연산을 지원한다. 
- 리스트는 큐의 모든 연산을 지원하지만 동적배열로 구현되어 있어 큐의 연산을 수행하기에는 효율적이지 않기 때문에, 큐를 위해서는 데크(Deque)라는 별도의 자료형을 사용해야 좋은성능을 기대할 수 있다.

### 스택(Stack)
- push(): 요소를 컬렉션에 추가한다.
- pop(): 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.

### 연결 리스트를 이용한 스택 ADT(Abstract Data Type) 구현
(1) 리스트를 담을 Node 클래스 정의

```c
class Node:
  def __init__(self, item, next):
      self.item = item
      self.next = next
```
- 초기화 함수 __init__() 에서 노드의 값은 item으로, 다음 노드를 가리키는 포인터는 next로 정의한다.

(2) Stack 클래스

```c
class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item):
        self.last = Node(item, self.last)
    
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item
```

- None <- 1 <- 2 <- 3 <- 4 <- 5 (last)
- stack은 각각 이전 값을 가리키는 연결 리스트로 구현되어 있으며, 가장 마지막 값은 last 포인터가 가리킨다.


### 문 20) 유효한 괄호(리트코드 20. Valid Parentheses)

### My solution)
```c
class Solution:  
    def toMatch(self, s:str) -> str:
        if s == ')':
            return '('
        if s == '}':
            return '{'
        if s == ']':
            return '['
    
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if len(stack)!=0 and (ch ==')' or ch == ']' or ch == '}'):
                if self.toMatch(ch) != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)     
 
        
        if not stack:
            return True
        else:
            return False
```

### Soultion 스택 일치 여부 판별)

```c
def isValid(self, s:str) -> bool:
    stack = []
    table = {
      ')' : '(',
      '}' : '{',
      ']' : '['
    }
    
    #스택 이용 예외 처리 및 일치 여부 판별
    
    for char in s:
       if char not in table:
          stack.append(char) # (, {, [
       elif not stack or table[char] != stack.pop():
           return False
       return len(stack) == 0
```

- 먼저 매핑 테이블을 만들어 놓고 테이블에 존재하지 않으면 무조건 push 하고, pop 했을 때 결과가 일치하지 않으면 False 를 리턴하도록 구현


### 문21) 중복 문자 제거(리트코드 316. Remove Duplicate Letters)

### Solution 스택을 이용한 문자 제거)

```c
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            
            # 이미 처리된 문자 여부 확인 위해 사용
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] >0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
```


### 문22) 일일 온도 (리트코드 739. Daily Temperatures)

### Solution 스택 값 비교)
```c
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        T = temperatures
        res = [0]*len(T)
        
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                res[last] = i-last
            
            stack.append(i)
        return res                     
```

- 현재의 인덱스를 계속 스택에 쌓아 두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도차이를 비교하여, 더 높다면 스택의 값을 pop()으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리한다. 


### 큐(Queue)
- 시퀀스의 한쪽 끝에는 entity를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 entity collection
- FIFO(First-In-First-Out, 선입선출) 로 처리되는, 줄을 서는 것에 비유할 수 있는 큐는 상대적으로 스택에 비해서는 쓰임새가 적다.
- 데크(Deque), 우선순위 큐, 너비 우선 탐색, 캐시 구현 등에 사용한다.
- 리스트는 큐의 모든 연산을 지원하지만 좀 더 나은 성능을 위해서는 양 방향 삽입, 삭제가 모두 O(1)에 가능한 데크(Deque)를 사용하는 편이 가장 좋다.


### 문24) 스택을 이용한 큐 구현(리트코드 232. Implement Queue using Stacks)

![2021-10-07 (3)](https://user-images.githubusercontent.com/74478432/136404645-29c04907-c29a-4f9a-a2ea-23a5f2959f65.png)

### Solution)

```c
class MyStack:

    def __init__(self):
        self.d = collections.deque()
        
    def push(self, x: int) -> None:
        self.d.append(x)
        for _ in range(len(self.d)-1): # 요소 삽입 후 맨 앞에 두는 재 정렬!
            self.d.append(self.d.popleft())

    def pop(self) -> int:
        return self.d.popleft()
        

    def top(self) -> int:
        return self.d[0]

    def empty(self) -> bool:
        return len(self.d) == 0
              
```









