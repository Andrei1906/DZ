def gip(i,j):
    'Функция вычиления гипотенузы'
    return (i**2 + j**2)**0.5
a,b = int(input()), int(input()) #катеты первого треугольника
x,y = int(input()), int(input()) #катеты второго треугольника
if gip(a,b)>gip(x,y):
    print('Гипотенуза первого больше, она равна: ',gip(a,b))
elif gip(a,b)==gip(x,y):
    print('Гипотенузы равны')
else:
    print('Гипотенуза второго больше, она равна: ',gip(x,y))