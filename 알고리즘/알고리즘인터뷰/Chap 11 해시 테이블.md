## Hash Table
- 해시 테이블 또는 해시 맵은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)을 구현하는 자료구조다.
- 해시 테이블의 가장 큰 특징은 대부분의 연산이 분할 상환 분석에 따른 시간 복잡도가 O(1)라는 점이다.

### 해시
- 해시 함수란 임의 크기 데이터를 고정 크기 값으로 매핑하는데 사용할 수 있는 함수를 말한다. 
- 해시 테이블을 인덱싱 하기 위해 해시 함수를 사용하는 것을 해싱(Hashing)이라 하며, 해싱은 정보를 가능한 한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법 중 하나이다

### 성능 좋은 해싱 함수의 특징
- 해시 함수 값 충돌의 최소화
- 쉽고 빠른 연산
- 해시 테이블 전체에 해시 값이 균일하게 분포
- 사용할 키의 모든 정보를 이용하여 해싱
- 해시 테이블 사용 효율이 높음

### 로드 팩터(Load Factor)
- 로드 팩터란 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것이다. 
- 로드 팩터 비율에 따라서 해시 함수를 재작성해야 될지 또는 해시 테이블의 크기를 조정해야 할지를 결정한다.
- 해시 함수가 키들을 잘 분산해 주는지를 말하는 효율성 측정에 사용한다. 
- 일반적으로 로드 팩터가 증가할 수록 해시 테이블의 성능은 점점 감소하게 된다. 

### 해시함수
- 해싱에는 다양한 알고리즘이 존재, 최상의 분포를 제공하는 방법은 데이터에 따라 제각각이다.
- 가장 단순하면서 널리 쓰이는 정수형 해싱 기법인 모듈로 연산을 이용한 나눗셈 방식: h(x) = x mod m
- h(x) 는 입력 값 x의 해시 함수를 통해 생성된 결과, m은 해시 테이블의 크기 

## 충돌(Collision)
(1) 개별 체이닝:
- 해시 테이블의 기본 방식. 충돌 발생 시 연결리스트로 연결 하는 방법
- 원리:
   - 키의 해시 값을 계산한다
   - 해시 값을 이용해 배열의 인덱스를 구한다
   - 같은 인덱스가 있다면 연결 리스트로 연결한다

- 잘 구현한 경우 대부분의 탐색은 O(1)이지만, 최악의 경우(Worst) 즉, 모든 해시 충돌이 발생했다고 가정할 경우에는 O(n)이 된다. 

(2) 오픈 어드레싱:
- 오픈 어드레싱(Open Addressing) 방식은 충돌 발생 시 탐사를 통해 빈 공간을 찾아나서는 방식이다.
- 사실상 무한정 저장할 수 있는 체이닝 방식과 달리, 오픈 어드레싱 방식은 전체 슬롯의 개수 이상은 저장할 수 없다.
- 충돌이 일어나면 테이블 공간 내에서 *탐사* 를 통해 빈 공간을 ㅊ자아 해결하며, 이 때문에 개별 체이닝 방식과 달리, 모든 원소가 반드시 자신의 해시값과 일치하는 주소에 저장된다는 보장은 없다.
- 선형 탐사 방식(Linear Probing): 충돌이 발생할 경우 해당 위치부터 순차적으로 탐사를 하나씩 진행한다. (특정 위치가 선점되어 있으면 바로 그 다음 위치를 확인하는 식)


### 언어별 해시 테이블 구현 방식:
- 해시 테이블로 구현된 파이썬의 자료형은 '딕셔너리'이다
- 파이썬은 충돌 시 '오픈 어드레싱' 방식을 사용한다. 


### 문1) 해시 맵 디자인(리트코드 706. Design HashMap)

``` C
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        

class MyHashMap:
    # 초기화 
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)      
    
    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        
        p.next = ListNode(key, value)

        
    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
        
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

```

- defaultdict(ListNode) 로 선언했기 때문에 존재하지 않는 인덱스를 조회할 경우 바로 빈 ListNode 생성


### 문29) 보석과 돌(리트코드 771. Jewels and Stones)

### My solution )

``` C
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = jewels
        s = stones
        freq = {} # dictionary
        
        for char in j:
            if char not in freq:
                freq[char] = 0
        for char in s:
            if char in freq:
                freq[char] += 1
        return sum(list(freq.values()))
```

- dict('{}') 이용하여 hashmap 구현 


### 문30) 중복 문자 없는 가장 긴 부분 문자열(리트코드 3. Longest Substring Repeating Characters)

``` C
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l =0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res
                
```


### 문31) 상위 K 빈도 요소(리트코드 347. Top K Frequent Elements)

### Solution (1) Counter를 이용한 음수 순 추출)

```c 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f],f))
        
        topk = list()
        # k번 만틈 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk

```

- 빈도 수를 키로 하고, freqs의 키를 값으로 했다 (즉, 키/값을 바꿔서 힙에 추가함)
- 힙은 키 순서대로 정렬되기 때문에 이를 위해 빈도 수를 키로 한 것이다.
- 파이썬 heapq 모듈은 최소 힙만 지원하기 때문에 값을 음수로 저장했다.


### Solution (2) 파이썬 다운 방식)

```c 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

```

### zip() 함수
- zip 함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할을 한다.

![2021-10-13](https://user-images.githubusercontent.com/74478432/136984252-b05bae18-a48f-40a1-9b25-af95a7e39140.png)

### 아스테리스크(*)

![2021-10-13 (1)](https://user-images.githubusercontent.com/74478432/136984424-70095070-2ed7-4ff6-a2e1-13c9dfdb125f.png)

- 파이썬에서 * 는 언팩이다. 
- 시퀀스 언패킹 연산자로 말 그대로 시퀀스를 풀어 헤치는 연산자를 뜻하며 주로 **튜플이나 리스트**를 언패킹하는데 사용한다.

![2021-10-13 (2)](https://user-images.githubusercontent.com/74478432/136984962-03cd35e4-f866-4609-83df-4991cddcf602.png)
- (1) 언패킹 안했을 때
- (2) 언패킹 했을 때


 





