### 배열
* 자료구조는 크게 메모리 공간 기반의 연속 방식과 포인터 기반의 연결 방식으로 나뉜다.
* 배열은 크기를 지정하고 해당 크기만큼의 연속된 메모리 공간을 할당 받는 작업을 수행하는 자료형을 말한다. 크기가 고정되어 있으며, 한번 생성한 배열은 크기를 변경하는 것이 불가능하다.
* 배열은 어느 위치에서나 O(1)에 조회가 가능하다.

### 동적 배열
* 파이썬에서는 **리스트**가 바로 동적 배열 자료형이다. 
* 미리 초깃 값을 작게 잡아 배열을 생성하고, 데이터가 추가 되면서 꽉 채워지면, 늘려주고 모두 복사하는 식이다. 대개는 '더블링' 이라 하여 2배씩 늘려주게 되는데, 당연히 모든 언어가 항상 
그런 것은 아니며 각 언어마다 늘려가는 비율은 상이하다.
* 동적 배열은 정적 배열과 달리 크기를 지정할 필요가 없어 매우 편리하게 활용할 수 있으며, 조회 또한 기존의 배영ㄹ과 동일하게 O(1)에 가능하다.
* 그러나 더블링이 필요할 만큼 공간이 차게 되면, 새로운 메모리 공간에 더 큰 크기의 배열을 할당하고 기존 데이터를 복사하는 작업이 필요하므로 O(n)비용이 발생한다. But, 자주 일어나는 일이
아니며, 분할 상환 분석에 따른 입력 시간은 여전히 O(1)이다. 

### 문7) 두 수의 합(리트코드 1. Two Sum)

### My Solution:

```c
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1. len(nums)):
                if nums[i] + nums[j] == target:
                   return [i,j]
```

* 브루트 포스로 계산, 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해 보는 무차별 대입 방식인 '브루트 포스'
* 비효율적인 풀이법, 최적화 필요
* 시간 복잡도 O(n^2)

### 교재 Solution(3) 첫 번째 수를 뺀 결과 키 조회:


```c
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, nums in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
               return [i, nums_map[target-num]]
```

* 딕셔너리는 해시테이블로 구현되어 있고, 이 경우 조회는 평균적으로 O(1)에 가능하다.

### 문8) 빗물 트래핑(리트코드 42. Trapping Rain Water):

### 교재 풀이(1) 투 포인터를 최대로 이동:

```c
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
           return 0
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left<right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
               volume += left_max - height[left]
               left += 1
            else:
               volume += right_max - height[right]
               right -= 1
        return volume
```


### 문9) 세 수의 합(리트코드 15. 3Sum)

### 풀이(2) 투 포인터 합 계산:

```c
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            # 중복된 값인 경우 continue로 건너 뛴다.
            if i>0 and nums[i] == nums[i-1]:
               continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # Sum이 0보다 작으면 값을 더 키워야 하므로 left를 우측으로 이동
                if sum < 0: 
                   left += 1
                # Sum이 0보다 크면 값을 더 작게 하기 위해 right를 좌측으로 이동
                elif sum > 0:
                   right -= 1
                
                # Sum=0 이면 정답이므로, 이 경우 결과를 리스트 변수 results에 추가 
                else:
                   results.append([nums[i], nums[left], nums[right]])
                   
                   # 중복 값 제거: 추가한 다음 left, right 양 옆에 동일한 값이 있을 수 있으므로 이를 left += 1, right -= 1로 반복해서 스킵하도록 한다. 
                   while left < right and nums[left] == nums[left+1]:
                       left += 1
                   while left < right and nums[right] == nums[right-1]:
                       right -= 1
                   left += 1
                   right -= 1
       return results
```

### 투 포인터:
- 대개 시작점 끝점 또는 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제풀이 전략
- 주로 정렬된 배열을 대상으로 하며, 2개의 포인터가 좌우로 자유롭게 움직이며 문제를 풀이한다. 


### 문10) 배열 파티션 I(리트코드 561. Array Partition I):


### 교재 풀이(1) 오름차순 풀이:

```c
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() = 0
        res = []
        for n in nums:
            res.append(n)
            if len(res) == 2:
               sum += min(res)
               res = []
        return sum
```
* min()을 합산 했을 때 최대를 만드는 것은 결국 min()이 되도록 커야 한다는 뜻이고, 뒤에서 부터 내림차순(또는 오름차순)으로 집어 넣으면 항상 최대 min() 페어를 유지할 수 있다.


### 교재 풀이(3) 파이썬 다운 방식:


```c
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum[sorted(nums)[::2]]
```

* 정렬된 상태에서는 짝수번째에 항상 작은 값이 위치한다. 
* 슬라이싱 구문[::2]는 2칸씩 건너 뛰므로 짝수번째를 계산하는 것과 동일하다.

.










