number = 15
size = 4
groups = 0

print("시작:", number)
while number >= size:
    number -= size
    groups += 1
    print(number + size, "-", size, "=", number, "(", groups, "번째 )")
    
print("더 못 빼는 이유: ", number < size)    
print("더 못 빼는 이유: ", number, "<", size)

print("몫(뺀 횟수) =", groups)

print("나머지(남은 수) =", number)