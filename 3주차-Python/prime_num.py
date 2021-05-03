def is_prime(num):
  # 들어온 num이 소수이면 True를 반환하고
  # 소수가 아니면 False를 반환하는 함수
  for i in range(2, num):
    if x % i == 0:
      return False #소수 아님
     else: 
      return True #소수임

def calculate_prime_number(length):
  # 소수를 2부터 length개만큼 담고 있는 배열을 반환하는 함수
  # 예를 들어 length에 2를 입력하면 [2, 3]을 반환하고
  # length에 5를 입력하면 [2, 3, 5, 7, 11]을 반환해야 함
  # is_prime 함수를 사용하면 편하게 코딩할 수 있음
  prime_array = [] #소수를 담은 배열 선언

n = int(input('Length?'))
print(calculate_prime_number(n))