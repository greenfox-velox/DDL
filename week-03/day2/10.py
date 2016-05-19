giraffe = {'color': 'yellow', 'pattern': 'polygonal patches'}

whale = {'color': 'blue', 'size': 10000}

print(giraffe)
print(giraffe['pattern'])

my_keys = ['color', 'pattern']

for key in my_keys:
    print(giraffe[key])

print(whale['size'])

whale['say'] = 'eeeeeeeeeeeeuuuuuuw'

print(whale)
