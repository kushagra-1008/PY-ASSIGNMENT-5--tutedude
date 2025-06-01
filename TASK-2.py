l = []
for i in range(1,11):
    l.append(i)
print(f'Original List: {l}')

a = l[0:5]
print(f'Extracted first five elements: {a}')

b = l[4::-1]
print(f'Reversed extracted elements: {b}')
