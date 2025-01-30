from sys import getsizeof

x = [i**2 for i in range (10000)]

def generatorFunction (inputNumber):
    for _ in range (inputNumber):
        yield _ ** 2

g = generatorFunction (10000)

print (f'Get size of list comprehension : {getsizeof (x)}')
print (f'Get size of generator : {getsizeof (g)}')

# def generatorSample (number):
#     for _ in range (number):
#         yield _

# # print (generatorSample (5))

# for i in generatorSample (5):
#     print (i)