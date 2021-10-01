a = str(input('Введите имя '))
b = str(input('Введите фамилию'))
c = int(input('Введите год рождения '))
print(a+'_'+b+'_'+str(c))
a,b=b,a
c+=60
print(a+'_'+b+'_'+str(c))