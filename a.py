def solution(value):
    num_str = str(value)
    count = 0
    sumstr = ''
    for i in num_str[::-1]:
        count += 1
        if count % 3 == 0 and count != len(num_str):
            i = ',' + i
            sumstr = i + sumstr
        else:
            sumstr = i + sumstr
    return sumstr

a = solution(1000)
print(a)
