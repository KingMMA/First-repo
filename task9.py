# Task 9
# 02.09.2023
# Кравченко Богдан

fr = 1
to = 2
num = 2
for i in range(2, 6):
    for _ in range(fr, to):
        num -= 1
        print(num, end=' ')
    print("")
    fr = to
    to += i
    num = to