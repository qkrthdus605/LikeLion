#H:시(0-23), M:분(0-59)

H, M = map(int, input().split())

if M < 45:
  if H == 0:
    H = 23   
    print(H, 60-(45-M))
  else:
    print(H-1, 60-(45-M))
else:
  print(H, M-45)