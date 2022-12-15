num1 = input().split()
num2 = int(input())
num2 = num2 % len(num1)
if num2 < 0:
    num2 = abs(num2)
    print(*num1[num2:], end=' ')
    print(*num1[0:num2])
    exit()

if num2 >= 0:
    num2 = abs(num2)
    print(*num1[-num2:], end=' ')
    print(*num1[0:-num2])
    exit()
