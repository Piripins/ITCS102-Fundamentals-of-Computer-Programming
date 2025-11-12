names = ['lei', 'aaron', 'Jay', 'Jana']

print(names)

print(names[2])
print(names[0 : 3])

names.append('Bjorn')
print(names)

names.pop()
print(names)

names.insert(2, 'pogi')
print(names)

names.remove('aaron')
print(names)

print(f'you have {len(names)} names')

names.sort()
print(names)

names.reverse()
print(names)

