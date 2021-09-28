### Linked List 

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




