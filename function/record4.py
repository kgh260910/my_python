record = {"x1": 0, "label": "car"}

#"label"키의 값 수정하기
record["label"] = "truck"
print(record["label"])

#특정 키에만 접근하기
print(record.get("note", "미제공")) #키 값으로 "note"가 없어서 "미제공"이 출력됩니다.

# 모든 키와 값에 접근하기
fruits = {"apple": 5, "banana": 3, "orange": 2}

keys = fruits.keys()       # 모든 키를 가져옴
print(keys)

values = fruits.values()   # 모든 값들을 가져옴
print(values)

items = fruits.items()     # 모든 키-값 쌍을 가져옴
print(items)

###################
index = 0

records = [{"x1": 0, "label": "car"}, {"x1": 0, "label": "person"}, {"x1": 0 , "label": "dog"}]
records[index]["label"] = "truck"
print(records[index]["label"])
print(records[1]["label"])
