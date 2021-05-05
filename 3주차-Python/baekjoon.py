#10869번
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#10430번
a, b, c = map(int, input().split())
print((a+b)%c) 
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c) 

#2588번
a = int(input())
b = input()
num1 = a * int(b[2])
num2 = a * int(b[1])
num3 = a * int(b[0])
result = a*int(b)
print(num1)
print(num2)
print(num3)
print(result)

