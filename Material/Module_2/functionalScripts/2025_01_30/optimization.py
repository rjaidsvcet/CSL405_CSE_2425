from sys import getsizeof

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map (lambda i : i **2, x)

print (y.__next__ ())
print ('For loop starts')
for i in y:
    print (i)

while True:
    try:
        value = next (y)
        print (value)
    except StopIteration:
        print ('While loop executed')
        break

# print (next (y))
# print (next (y))
# print (next (y))
# print (next (y))
# print ('Some random line')
# for _ in y:
#     print (list (y))

# print ('{}'.format (getsizeof (y)))
# print ('{}'.format (getsizeof (list (y))))

# print (f'The size of list : {getsizeof(x)}')
# print (f'The size of range : {getsizeof (range (1, 11))}')

# for element in x:
#     print (element)

# for i in range (1, 11):
#     print (i)