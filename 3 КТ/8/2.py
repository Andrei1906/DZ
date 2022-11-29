str1 = input()
str2 = str1.lower().split()     #создаем копию заданной строки, только все буквы делаем маленькими, чтобы не учитывать регистр
for i in range(len(str2)):
    str2[i] = sorted(str2[i])   #сортируем символы каждого слова по алфавиту
for k in range(len(str2)):
    str2[k]=''.join(str2[k])    #соединяем символы в слове
str1 = str1.split()
#Пишем цикл нахождения и замены заглавных букв:
for j in range(len(str1)):
    for k in str1[j]:
        if k.isupper():
            str2[j] = str2[j].replace(k.lower(),k.upper(),1)
print(' '.join(str2))