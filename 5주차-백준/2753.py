#연도(1이상 4000이하의 자연수)가 주어졌을 때 윤년이면 1, 아니면 0출력

year = int(input())

if (year%4==0 and year%100 != 0) or year%400 == 0:
  print("1")
else:
  print("0")