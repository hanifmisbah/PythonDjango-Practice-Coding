print('(Python Identity Operators)')
a = [1, 4, 2, 5]
z = ['Alfa', 'Beta', 'Teta', 'Gama']
q = z
print(' ')
print(z is q)
print(z == a)
print(' ')
print('(Python Logical Operators)')
x = 5
print(x > 3 and x < 10)
print(' ')
x = 5
print(x > 3 or x < 4)
print(' ')
x = 5
print(not(x > 3 and x < 10))
print(' ')
print('(Python Membership Operators)')
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" in x)
print(' ')
x = ["apple", "banana"]
print("pineapple" not in x)
x = 5
x <<= 3
print(x)