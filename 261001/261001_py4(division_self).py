# number = 15
# size = 4
# groups = 0
# 
# while number >= size:
#     number -= size
#     groups += 1
#     print(number + size, "-", size, "=", number, "(", groups, "번째 )")
#     
# print("더 못 뺀 이유: ", number, "<", size)
# print("몫 =", groups)
# print("나머지 =", number)
#           
# print("---구분선---")    
#     
# number = 20
# 
# print(number % 10)
# print(number // 2)
# print(number // 2 // 2 )
# print(number ** 3)
# 
# print("---구분선---")
# 
# number = 200
# groups = 0
# 
# while number >= 25:
#     number -= 25
#     groups += 1
#     print(number + 25, "-", 25, "=", number, "(", groups, "번째 )")
#     if number % 100 == 0 :
#         print(groups,"번 나누면", "남은 수가 100의 배수인 때")
# 
# 456명의 선수를 절반씩 나누는 방법? 그리고 몇 번 나누면 끝이나나
# 특정 라운드 종료시 각 인원에게 지급되는 금액

player = 456
ending = 5
round = 1
prize_money = 45600000000  # 총 상금 456억 원

print("오징어 게임 시작")
while player >= ending:
    player //= 2
    print("round :", round, "살아남은 인원:" ,player)
    current_money = prize_money // player
    print("각 인원에게 배분되는 상금: ", current_money, "원")
    
    round += 1

    
        
