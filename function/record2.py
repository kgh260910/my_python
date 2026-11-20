# record = {"x1": 0, "label": "car"}
# for key2, value3 in record.items():
#     print(key2, value3)

records = [{"x1": 0, "label": "car"}, {"x1": 0, "label": "person"}]

for record in records:
    for key3, value4 in record.items():
        print(key3, value4)

print("*********************")

records = [{"label": "car", "inside": False}, {"label": "drone", "inside": True}]
count = 0
for record in records:
    print(record["label"], record["inside"])
    if record["label"]:
        count += 1
print("구역 안: ", count)
