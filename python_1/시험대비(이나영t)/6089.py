#시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

a,r,n = map(int,input().split())

for i in range(2, n+1):
  a *= r
  2
print(a)