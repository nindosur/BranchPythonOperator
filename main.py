# 1
value1 = int(input("Введите номер дня недели: "))
if(value1==1):
    print(value1, "- это понедельник.")
elif(value1==2):
    print(value1, "- это вторник.")
elif(value1==3):
    print(value1, "- это среда.")
elif(value1==4):
    print(value1, "- это четверг.")
elif(value1==5):
    print(value1, "- это пятница.")
elif(value1==6):
    print(value1, "- это суббота.")
elif(value1==7):
    print(value1, "- это воскресенье.")
else:
    print("В неделе 7 дней!!!")

# 2
value2 = int(input("Введите номер месяца: "))
if(value2==1):
    print(value2, "- январь.")
elif(value2==2):
    print(value2, "- февраль.")
elif (value2 == 2):
    print(value2, "- февраль.")
elif (value2 == 3):
    print(value2, "- март.")
elif (value2 == 4):
    print(value2, "- апрель.")
elif (value2 == 5):
    print(value2, "- май.")
elif (value2 == 6):
    print(value2, "- июнь.")
elif (value2 == 7):
    print(value2, "- июль.")
elif (value2 == 8):
    print(value2, "- август.")
elif (value2 == 9):
    print(value2, "- сентябрь.")
elif (value2 == 10):
    print(value2, "- октябрь.")
elif (value2 == 11):
    print(value2, "- ноябрь.")
elif (value2 == 12):
    print(value2, "- декабрь.")
else:
    print("В году всего 12 месяцев!!!!")

# 3
value3 = int(input("Введите число: "))
x = 0
if(value3>x):
    print("Number is positive")
elif(value3<x):
    print("Number is negative")
else:
    print("Number is equal to zero")

# 4
value4 = int(input("Введите первое число: "))
value5 = int(input("Введите второе число: "))
if(value4==value5):
    print("Числа равны.")
else:
    print(min(value4,value5),max(value4,value5))


