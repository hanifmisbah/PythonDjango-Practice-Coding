tel = {'jack':4231, 'sape':1912}
tel['guido'] = 3213
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 7627
print(tel)
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)
print('========================')
print(dict([('sape', 1912), ('guido', 3213), ('jack', 4231)]))
dict = {x: x**2 for x in (2, 3, 4)}
print(dict)
dict(sape=1912, guido=3213, jack=4231)
print(dict)

