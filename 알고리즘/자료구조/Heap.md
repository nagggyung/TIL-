## ADT (Abstract Data Type) : Priority Queue(우선순위 큐)
- 일정한 규칙에 의하여 먼저 나가는 숫자가 정해진 큐
- 우선 순위 큐 Structure 구현 시 Heap 사용

- ex)  가장 큰 숫자를 먼저 빼주는 큐
[ 3 5 7 9 ] =>(deque) [9 7 5 3 1]

## Heap
- 완전 이진 트리(Complete Binary Tree) 통해 구현 
- maxHeap: 부모노드는 자식노드 보다 항상 크다 ( P > child nodes)
- minHeap: 부모노드는 자식노드 보다 항상 작다 ( P < child nodes)
- Complete binary tree 성질을 사용하면 배열로도 Heap을 표현할 수 있다.

![2021-10-12](https://user-images.githubusercontent.com/74478432/136897037-f7f3230c-c27d-455b-b17d-2e1ed827b446.png)

[ 9 7 5 1 3 ]

- 어떤 노드에서 부모노드로 가기 위한 공식: (idx-1)/2
- 부모노드에서 left child로 도달하는 공식: 2 x idx + 1
- 부모노드에서 right child로 도달하는 공식: 2 x idx + 2

### Time complexity:
- add: O(logn)
- delete: O(logn)
- Top: O(1)
- Build Heap: O(n)

### 문1) Find K'th smallest number
- 작은 숫자 순서로 sorting k번째 숫자 return 

```c

import heapq

nums = [9,7,5,3,1]
heapq.heapify(nums)

# 3rd smallest num
heapq.heappop(nums)
heapq.heappop(nums)
print(nums[0])

```


### 문2) k개의 큰 숫자 찾기
- minHeap 이용, 공간 복잡도 문제 해결


```c
import heapq

nums = [1,3,5,7,9,11]
print(nums)

large_nums = []

for num in nums:
  heapq.heappush(large_nums,num)
  if 3 < len(large_nums):
    heapq.heappop(large_nums)
print(large_nums)

```

### 문3) Top K Frequent Element
- heap solution

```c

from typing import List
from collections import defaultdict
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
  if k == 0:
    return []
  
  #hash map
  count_map = defaultdict(int)

  #count over nums
  for num in nums:
    count_map[num] += 1


  #fixed size heap
  topK_heap = []
  for num in count_map:
    heapq.heappush(topK_heap,(count_map[num],num))  #use hashmap count as comp
    if k < len(topK_heap):
      heapq.heappop(topK_heap)
      
  #return list
  topK = []
  for count,num in topK_heap:
    topK.append(num)
    
  return topK


topK = topKFrequent(nums=[1,3,5,3,9,3,7,5], k = 2 )
print(topK)
  
```














