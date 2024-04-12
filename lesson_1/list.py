lst=[1, 2, 3, 4, 5, 6]
dct={'name': 'Anna', 'age': 4}
name= 'Anna'
tpl = ('n', 'a', 'A')

result= dct['age'] in lst and dct['name'] in tpl
print(result)


print(dct['name'] == name and dct['age'] in lst)

print(len(name))
print(name.upper())
name= name.lower()
print(name)

name = name.capitalize()
print(name)


name = name.replace('n', 'a')
print(name)


str = 'Hello world' 
str = str.split()   #зробити список із стоки розбивши речення
print(str)
print(type(str))

string = " ".join(str)
print (string)

string = string.count('l')
print ('Count of litters is ', string)

# зміна типів з int у str
string = 1 
string = float(string)
print(type(string))
