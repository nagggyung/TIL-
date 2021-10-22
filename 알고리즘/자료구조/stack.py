'''
Stack
- 먼저 들어온 데이터가 나중에 나가는 형식(선입 후출)
- 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있다.
- 스택 동작: 삽입(push), 삭제(pop)
- 스택은 리스트 자료형으로 구현 가능(리스트: append(), pop() 함수 이용)
'''

# 리스트 자료형으로 stack 구현가능
stack = [] 

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
