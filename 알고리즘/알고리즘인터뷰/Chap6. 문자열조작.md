### 1) 유효한 팰린드롬(리트코드: 125. Valid Palindrome)
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


