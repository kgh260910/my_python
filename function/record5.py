fruits = {"apple": 5, "banana": 3}

# 새로운 키-값 쌍 추가
fruits["orange"] = 2

print(fruits)  # 출력: {'apple': 5, 'banana': 3, 'orange': 2}

# key와 value가 하나의 리스트에 저장되어 있는 경우
items = [("apple", 3), ("banana", 5), ("orange", 7)]
fruit = dict(items)
print(fruit)

# key와 value가 각각의 리스트에 저장되어 있는 경우
fruit_names = ["apple", "banana", "orange"]
fruit_counts = [3, 5, 7]
fruits = dict(zip(fruit_names, fruit_counts))
print(fruits)
