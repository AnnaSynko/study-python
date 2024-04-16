test_list=[1, 2, 3, 4, 5, 6]

for i in test_list:
    print('i =', i)


# while
#test_1
a = 0
while a < 10:
    a+=1
    print(a) 

#test_2
b = 0
while b < 5:
    print(b)
    b +=1

#Test_3
while len(test_list) < 10 :
    test_list.append(3)
    print(test_list)   

# FOR
test_2_list = ["test", "python", "code"]

for s in test_2_list:
    print("Cписок", s)
    if s==test_2_list[0] :
        print(s)
    elif s == test_2_list[1] :
        print(s)
    else : print(s)

# WHILE
c = 0
add_list = []
while len(add_list) < 10 :
 add_list.append(c)
 c += 1
 print (c)
 if len(add_list) == 5: print("You are at middle of list")
 