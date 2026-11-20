record = {"x1": 0, "label": "car"}

record["label"] = "truck"
print(record["label"])
print(record.get("note", "미제공")) #키 값으로 "note"가 없어서 "미제공"이 출력됩니다.