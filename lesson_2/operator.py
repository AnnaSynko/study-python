string= "Hello world"

if "Hellllo" in string:
    print("Hello in string")
elif "world" in string:
    print("word in string")
else: print("No")

# Task2
a = 10
b = 20
if a < b or b == 20 and b != 20:  # True OR False  тому True
    print(a+b)
else: print('False')


# Task_3
test_list = ['hello', 'testt', 1, 2, 3]

if "helllo" in test_list and 1 in test_list:
    print("That`s true")
elif "test" not in test_list:
    print("Test not in LIST")
else: print('That is false')


# Task_4
user_1= {
    #"name": "Anna",
    "age": 27,
    "balance": 20000,
    "currency": "USD",
    "status": True
}

user_2= {
    "name": "Ben",
    "age": 21,
    "balance": 15000,
    "currency": "EUR",
    "status": False
}

user_3= {
    "name": "John",
    "age": 23,
    "balance": 5000,
    "currency": "UAH",
    "status": True
}

list_of_currency= ['USD', 'EUR', 'GBR', 'UAH']

if user_1.get('name', None) and user_1['status']==True:
    if user_1['balance'] > 100000 and user_1['currency'] in list_of_currency:
        print("Welcome")
    else: print("Money critical not enough")
elif not user_1.get('name', None): print("write your name ")
elif user_1['age'] < 18:
    print("For registry binance account you have to be 18 year old")

else: print ("Something went wrong")