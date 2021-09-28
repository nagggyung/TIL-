## Linked List

- Link 이용해서 List 만듦
- Node로 이루어져 있다.
- val, ref(addr) 값 존재
- Linked List 종류: Singly Linked List, Doubly Linked List
- 첫 번째 Node: head(Linked List의 시작 점)
- Find: O(n) why? Linked List는 Random access를 제공하지 않는다.
- node insertion: O(1)
- node deletion: O(1)
- 노드 삽입, 삭제, 탐색, 역순으로 바꾸기 등을 암기 수준으로 알고 있어야 함! 

### 1) Singly Linked List 

ex) 1,2,3,4

![linked_list_자료1](https://user-images.githubusercontent.com/74478432/135080765-83dd85e3-f701-47a8-80af-95a50e1a3869.jpg)

- head node 부터 시작해서 각 노드는 value 값 존재, ref(addr) 부분 다음 노드(next) 가리킨다.

### 2) Doubly Linked List

ex) 1,2,3,4

![linked_list_자료2](https://user-images.githubusercontent.com/74478432/135080778-a598e597-e2bd-4fd9-b9f7-1a76243cbc1f.jpg)

- head node, tail node 존재, 양 방향으로 이동 가능 

### 3) Singly Linked List Implementation 

(1) Linked List class 생성

```c
class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
```
(2) Node 생성 및 연결 

```c
head_node = ListNode(1) # head_node 생성하여 value 값으로 1을 넣어준다.
head_node.next = ListNode(2) # value가 2인 node가 생성되고 head_node의 next는 새로 생성된 node를 가리킨다. 
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)
```

(3) Linked List - print
- Iterative way of printing nodes in Linked List
- Recursive way of printing nodes in Linked List

```c
# Iterative way of printing nodes in Linked List

def printNodes(node: ListNode):
  crnt_node = node
  while crnt_node is not None:
    print(crnt_node.val, end=' ')
    crnt_node = crnt_node.next # crnt_node update to the next node
```

![image](https://user-images.githubusercontent.com/74478432/135081374-3c09ab74-f359-4d42-a9fa-d25c8d0e3f96.png)


```c
# Recursive way of printing nodes in Linked List

def printNodesRecur(node:ListNode):
  print(node.val, end = ' ')
  if node.next is not None:
    printNodesRecur(node.next)
```

![image](https://user-images.githubusercontent.com/74478432/135081528-340e27ec-c3ca-46ce-a5df-a5c507018370.png)


### Linked List: 노드 들을 묶어서 전체적인 Class 만들기
Class:
- add at head
- add at Back/After
- FindeNode
- DeleteAfter

**class 생성/printNodes code**

```c
class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

def printNodes(node:ListNode):
  crn_node = node
  while crn_node is not None:
    print(crn_node.val, end = ' ')
    crn_node = crn_node.next
```


1) AddAtHead(self, val):

- AddAtHead(1)
![2021-09-29](https://user-images.githubusercontent.com/74478432/135129885-707c96f5-3a01-401d-a245-26cf3210a3da.png)

- AddAtHead(2)
![2021-09-29 (1)](https://user-images.githubusercontent.com/74478432/135130097-92c93951-0912-4d68-9e42-c59ff2765283.png)

- code: 
```c
# value 와 next가 들어있는 node를 이용해서 그들 list class를 만들어 보자

class SLinkedList:
  def __init__(self):
    self.head = None
  
  def addAtHead(self, val):  # O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node
    
```

2) addBack(self, val):
- addBack(3)
![2021-09-29 (2)](https://user-images.githubusercontent.com/74478432/135130674-2f2bdaf2-855e-4de4-89e1-bd79b904ef1d.png)

- code:
```c
class SLinkedList:
  def __init__(self):
    self.head = None
  
  def addAtHead(self, val):  # O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node
  
  # edge case 고려 x
  def addBack(self, val): # O(n)
    node = ListNode(val)
    crn_node = self.head
    while crn_node.next is not None:
      crn_node = crn_node.next
    crn_node.next = node 
    
```

3) findNode(self, val):
- findNode(1)
![2021-09-29 (4)](https://user-images.githubusercontent.com/74478432/135130952-ffb162ba-c8f8-446d-a571-41b2d8f3ebb1.png)

- code:
```c
class SLinkedList:
  def __init__(self):
    self.head = None
  
  def addAtHead(self, val):  # O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node
  
  # edge case 고려 x
  def addBack(self, val): # O(n)
    node = ListNode(val)
    crn_node = self.head
    while crn_node.next is not None:
      crn_node = crn_node.next
    crn_node.next = node 
  
  def findNode(self, val): # O(n)
    crn_node = self.head
    while crn_node is not None:
      if crn_node.val == val:
        return crn_node
      crn_node = crn_node.next
    raise RuntimeError('Node not found')
    # 예외를 일으키고 싶으면 raise 문을 사용!
    
```

4) addAfter(node1, val):
- addAfter(node1, 4)
![2021-09-29 (5)](https://user-images.githubusercontent.com/74478432/135131334-b8803d69-2492-4d16-b68b-ad3d871979f4.png)

- code:
```c
class SLinkedList:
  def __init__(self):
    self.head = None
  
  def addAtHead(self, val):  # O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node
  
  # edge case 고려 x
  def addBack(self, val): # O(n)
    node = ListNode(val)
    crn_node = self.head
    while crn_node.next is not None:
      crn_node = crn_node.next
    crn_node.next = node 
  
  def findNode(self, val): # O(n)
    crn_node = self.head
    while crn_node is not None:
      if crn_node.val == val:
        return crn_node
      crn_node = crn_node.next
    raise RuntimeError('Node not found')
  
  def addAfter(self, node, val): # prev node가 함께 넘어오기 때문에, O(1)
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node
    
```

5) deleteAfter(self, prev_node) 
- deleteAfter(node1)
![2021-09-29 (6)](https://user-images.githubusercontent.com/74478432/135131663-bf712053-644a-40ee-8e2d-7f28d2a0d3f2.png)

- code:
```c
class SLinkedList:
  def __init__(self):
    self.head = None
  
  def addAtHead(self, val):  # O(1)
    node = ListNode(val)
    node.next = self.head
    self.head = node
  
  # edge case 고려 x
  def addBack(self, val): # O(n)
    node = ListNode(val)
    crn_node = self.head
    while crn_node.next is not None:
      crn_node = crn_node.next
    crn_node.next = node 
  
  def findNode(self, val): # O(n)
    crn_node = self.head
    while crn_node is not None:
      if crn_node.val == val:
        return crn_node
      crn_node = crn_node.next
    raise RuntimeError('Node not found')
  
  def addAfter(self, node, val): # prev node가 함께 넘어오기 때문에, O(1)
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

  def deleteAfter(self, prev_node): # prev node가 함께 넘어오기 때문에, O(1)
    if prev_node.next is not None:
      prev_node.next = prev_node.next.next
    
```

6) result:

![2021-09-29 (7)](https://user-images.githubusercontent.com/74478432/135131803-b5f907b6-9ebf-4950-8666-335745cc1aea.png)





