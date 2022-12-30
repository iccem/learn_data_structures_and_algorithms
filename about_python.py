t = [1, 2, 3, 4, 5, 6, 7]
a, b, *rest = t

print(a)
print(b)
print(rest)

print(t)
print(*t, sep=':', end='!\n')
