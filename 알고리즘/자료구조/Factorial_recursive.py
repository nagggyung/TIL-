'''
재귀 함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- DFS 구현시 사용
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시 하지 않으면 함수가 무한히 호출될 수 있다.
'''

# 반복적으로 구현한 N!
def factorial_iterative(n):
  result = 1
  # 1 부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n+1):
    result*=i
  return result

# 재귀적으로 구현한 N!
def factorial_recursive(n):
  if n <=1: # n이 1 이하인 경우 1을 반환
    return 1
  
  # n! = n*(n-1)! 를 그대로 코드로 작성하기
  return n*factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n=5)
print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))




