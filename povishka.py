#Даны цифры двух десятичных целых чисел: трехзначного и двузначного , где а1 и в1 – число единиц, а2 и в2 – число десятков,а3 – число сотен. Получить цифры числа, равного сумме заданных чисел (известно, что это число трехзначное). Числа-слагаемые и число-результат не определять; условный оператор не использовать.
a1 = int(input('a1-число единиц='))
a2 = int(input('a2-число десятков='))
a3 = int(input('a3-число сотен'))
b1 = int(input('b1-число единиц= '))
b2 = int(input('b2-число десятков='))
a = a1 / 100
b = b2 / 10
c = a3 % 100 % 10
s = a + b + c
print('Полученные цифры числа',s)


