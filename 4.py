years= int(input('Введите число лет  '))
exp = int(input('Введите число экспонатов  '))
a = int(years*365*24//(8*(60/5)))
b = int(exp//(8*(60//5)//365)
print('Количество экспонатов ',a)
print('Количество часов ',b)