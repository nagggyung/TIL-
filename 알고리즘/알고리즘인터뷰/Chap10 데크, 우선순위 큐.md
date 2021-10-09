### Chap10 데크, 우선순위 큐

### 데크(Deque):
- 데크(Deque)는 더블 엔디드 큐(Double-Ended Queue)의 줄임말로, 글자 그대로 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)이다.
- 데크는 양쪽에서 삭제와 삽입을 모두 처리할 수 있으며, 스택과 큐의 특징을 모두 갖고 있다.
- 파이썬은 데크 자료형을 다음과 같이 collections 모듈에서 deque라는 이름으로 지원한다.

>>> import
>>> d = collections.deque()
>>> type(d)
<class 'collections.deque'>

