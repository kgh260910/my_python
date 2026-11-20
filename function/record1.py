# Record
record =  {"x1": 0, "y1": 400, "x2": 200, "y2": 600, "label": "car"}
print(record["label"])     # car 출력
print(record["x1"])        # 0   출력
print(record["y2"])        # 600 출력

record2 = {"x1": 100, "y1": 200}

# Record들의 묶음
records = [record, record2]
print(records)            # record,record2 출력
print(records[1])         # record2 출력
print(records[1]["x1"])   # record2의 "x1"키의 값 출력
print(records[1][0])    # KeyError : 0



