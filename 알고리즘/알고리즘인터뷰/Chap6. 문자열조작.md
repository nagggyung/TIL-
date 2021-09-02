### 문1) 유효한 팰린드롬(리트코드: 125. Valid Palindrome)
* '팰린드롬'이란, 앞 뒤가 똑같은 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장을 의미한다.

### My solution:

```c
class Solution:
  def isPalindrome(self, s:str) -> bool:
    arr =[]
    for c in s:
      if c.isalpha():
        arr.append(c.lower())
      if c.isdigit():
        arr.append(c)
   
   for c in range(len(arr)):
      if arr[c] != arr[(len(arr)-1)-c]:
        return False
   return True
```

### Used Function For solution:
* isalpha(): 문자열의 구성이 알파벳 or 한글 인지 확인 하는 함수. 알파벳 or 한글인 경우 'True' 리턴, but 공백, 기호, 숫자가 있는 경우 'False'를 리턴한다.
* isdigit(): 문자열의 구성이 숫자인지 확인 하는 함수. 공백, 문자, 기호가 있는 경우 'False' 리턴.
* isalnum(): 알파벳(한글) 또는 숫자인지 확인하는 법. 기호 또는 공백이 포함된 경우 'False' 리턴.
* upper(): 대문자로 변경하는 함수.
* lower(): 소문자로 변경하는 함수.
* isupper(): 대문자인지 확인하는 함수.
* islower(): 소문자인지 확인하는 함수.

### 교재 Solution(1) 데크 자료형을 이용한 최적화:

```c
class Solution:
  def isPalindrome(self, s:str) -> bool:
    #자료형 데크로 선언
    strs: Deque = collections.deque()
    
    for char in s:
      if char.isalnum():
         strs.append(char.lower())
    while len(strs)>1:
      if strs.popleft() != strs.pop():
         return False
    return True
```

### Queue vs Deque:

* 큐(Queue):
선형리스트의 한쪽에서는 삽입(PUSH), 다른 한 쪽에서는 삭제(POP) 작업이 이루어지도록 구성한 자료구조.

* 데크(Deque):
삽입(PUSH)과 삭제(POP)가 리스트의 양쪽 끝에서 모두 발생할 수 있는 자료구조.

### 교재 Solution(2) 슬라이싱 사용:

```c
class Solution:
  def isPalindrome(self, s:str) -> bool:
      s = s.lower()
      # 정규식으로 불필요한 문자 필터링
      s = re.sub('[^a-z0-9]', '', s)
      
      return s == s[::-1] #슬라이싱
```


### 문자열 슬라이싱

EX) 안녕하세요

* s[:] == '안녕하세요'
* s[::1] == '안녕하세요' : 1은 기본 값으로 동일하다.
* s[::-1] == '요세하녕안': 뒤집는다. 


### 문3) 로그파일 재정렬(리트코드: 937. Reorder Log Files)

### 교재 Solution(1) 람다 + 연산자 이용:

```c
class Solution:
  def reorderLogFiles(self, logs:List[str]) -> List[str]:
      letters, digits = [], []
      for log in logs:
          if log.split()[1].isdigit():
              digits.append(log)
          else:
              letters.append(log)
      letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 식별자를 제와한 문자열[1:]을 키로하여 정렬, 동일한 경우 후 순위로 식별자[0]을 지정해 정렬되도록 구현
      return letters + digits
```

### 문4) 가장흔한 단어(리트코드 819. Most Common Word)

### My solution:

```c
class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      for s in paragraph:
          if s.isalnum() == False:
             paragraph = paragraph.replace(s, " ")
      
      paragraph = paragraph.lower().split()
      words = collections.Counter(paragraph)
      
      for word in banned:
          if word.lower() in paragraph:
             del words[word.lower()]
          return words.most_common(1)[0][0]
```

### 교재 Solution(1) 리스트 컴프리헨션, Counter 객체 사용:

```c
class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]
      # 정규식에서 '\w'는 단어 문자(word character)을 뜻하며, ^은 not을 의미한다. 
      # 따라서 위의 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.
      
      counts = collections.Counter(words)
      return counts.most_common(1)[0][0]
```

### 문5) 그룹 애너그램(리트코드 49. Group Anagrams)
애너그램이란, 일종의 언어 유희로서 문자를 재 배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.

###  sort vs sorted:
(1) sort(): 리스트 정렬/none 리턴<br>
(2) sorted():<br> 
- 리스트, 문자열, 튜플, 딕셔너리 등 반복가능한 자료형 모두 가능
- 기존 리스트를 복사해서 새로 만들어 반환(기존 리스트에는 영향을 주지 않는다)
- 리스트로 결과를 리턴

### 교재 Solution(1) 정렬하여 딕셔너리에 추가

```c
class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # 해당 키에 대한 기본 값을 비어있는 리스트로 세팅
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
```

애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다. 애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 된다. <br>
sorted()는 문자열도 잘 정렬하여 결과를 리스트 형태로 리턴하는데, 이를 다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구현한다. 
애너그램 끼리는 같은 키를 갖게되고 따라서 여기에 append()하는 형태가 된다. 이 처럼 정렬한 값을 키로 하여 딕셔너리에 추가한다. 만약 존재하지 않는 키를 삽입하려 할 경우 KeyError가 발생하므로, 에러가 나지 않도록 defaultdict()로 선언하며, 매번 키 존재 여를 체크하지 않고 비교구문을 생략해 간결하게 구성한다. 
