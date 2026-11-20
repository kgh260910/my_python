record = {"x1": 0, "label": "car"}

record["label"] = "truck"
print(record["label"])

print(record.get("note", "미제공")) #키 값으로 "note"가 없어서 "미제공"이 출력됩니다.

# index = 0
#
# records = [{"x1": 0, "label": "car"}, {"x1": 0, "label": "person"}, {"x1": 0 , "label": "dog"}]
# records[index]["label"] = "truck"
# print(records[index]["label"])
# print(records[1]["label"])
