def make_speedup(count, start, step):
    result = []
    for i in range(count):
        result.append(start - i * step)
    return result

fast = make_speedup(6, 600, 100)
print(fast)
print(result)
#result는 make_speedup 함수 안에서만 만들어진 내부 변수이기 때문에
#해당 변수를 찾을 수 없다며 NameError: name 'result' isn't defined
#오류가 나타납니다.