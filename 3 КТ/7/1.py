n = int(input('введите длину массива: ')) #задаем длину массива
print('введите элементы массива: ')
d = [] #создаем пустой массив
sum = 0
for j in range(n):
     x = int(input())
     if j%2!=0:      #проверяем четный ли индекс
         sum = sum +x    #если нечетный - добавляем
     d.append(x) #добавляем элемент в массив
print('Массив D: ', d)
print('Сумма:', sum)