from collections import Counter
d1 = {'ключ1': 50, 'ключ2': 100, 'ключ3':200}
d2 = {'ключ1': 200, 'ключ2': 100, 'ключ4':300}
new_dict = Counter(d1) + Counter(d2)
print('='*30)
print('\n'*3)
print(new_dict)
print('\n'*3)
print('='*30)