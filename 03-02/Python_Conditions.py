print('(Python Identity Conditions)')
k = "Keterangan : "
a = input(int)
b = input(int)
if b > a:
	print(k,"b is greater than a")
elif a == b:
	print(k,"a and b are equal")
else:
 	print(k,"a is greater than b")
print(' ')
print('(Python Identity Conditions)')
a = input(int)
b = input(int)
c = input(int)
if a > b and c > a:
 	print(k,"Both conditions are True")
else:
 	print(k,"One conditions are False")
print(' ')
d = input(int)
e = input(int)
f = input(int)
if d > e or d > f:
 	print(k,"At least one of the conditions is True")
else:
 	print(k,"One conditions are False")