num_1 = 5
num_2 = 5.25
string = 'Anna'
num_3 = True
lists= [ 0, 1, 3, 4, 5, 6]
dictionary = {'name': 'Anna', 'city': 'Lviv', 'age': 27}
tuple = (0, 1, 2)
num_4 = None

print(type(num_1))
print(type(num_2))
print(type(string))
print(type(num_3))
print(type(lists))
print(type(dictionary))
print(type(tuple))
print(type(num_4))

print(num_1 < num_2)
print(num_1 == num_2)
print(int(num_2))
print(num_1 == int(num_2))

print(string == num_3)
print(num_1 in lists)  # чи є число 5 у списку

print(string in dictionary['name'])

print(lists[0] in tuple) # чи є значення 1 в кортежі
#ставимо запитання з одного боку має бути конкретне значення а з іншого список значень

print(dictionary['age'])
print(dictionary['age'] == 27)
print(dictionary['age'] > num_1)
print(dictionary['age'] in lists)
print(dictionary['age'] in tuple)

print('A' in dictionary['name'])

