'''
재귀 함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- DFS 구현시 사용
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시 하지 않으면 함수가 무한히 호출될 수 있다.
'''

def gcd(a, b):
  if a%b == 0: ## a가 b의 배수라면
    return b
  else:
    return gcd(b, a%b)
  
print(gcd(192, 162))
