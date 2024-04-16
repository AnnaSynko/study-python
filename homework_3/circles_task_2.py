#Сума елементів у списку
list = [1, 2, 3, 4, 5, 6]
sum = 0
for number in range(6):
    sum += list[number] 
    print(f"Iteration {number} = ", sum)
