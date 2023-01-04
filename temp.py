class Someone:
    a = 0
    
    def func(self):
        a = 1
        
b = Someone()

print('-'* 20)
print(f'print: {b.a}')