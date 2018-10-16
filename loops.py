animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)