base_dic ={'name': 'Tom', 'age': 40, 'high': 180}
print(base_dic.keys())
print(base_dic.values())

print(base_dic.items())

print(base_dic['name'])  #отримати значення згідно вказаного ключа
print(base_dic['name'], base_dic.get('name'))

print(base_dic['name'], base_dic.get('is_animal', 'No'))

# print(base_dic['is_animal'])  -помилка за відсутності такого ключа у словнику