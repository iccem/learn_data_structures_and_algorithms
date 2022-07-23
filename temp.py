s = input().lower().split()
d = {}

for i in s:
    if i in d:
        d[i] += 1
    elif i not in d:
        d[i] = 1

