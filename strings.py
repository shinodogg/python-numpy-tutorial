hello = 'hello'
world = "world"
print(hello)
print(len(hello))
hw = hello + ' ' + world
print(hw)
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)

s = "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('      world  '.strip())