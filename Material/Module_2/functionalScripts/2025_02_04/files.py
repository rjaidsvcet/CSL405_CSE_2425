# Writing in the file 

file = open ('./file.txt', 'w')
file.write ('Hello World')
file.close ()

# Reading in the file

file = open ('./file.txt', 'rb')
content = file.read ()
print (content)
file.close ()

# Appending to existing file

file = open ('./file.txt', 'a')
file.write ('\nAdding some new line')
file.close ()

### Dealing with open files

file = open ('./file.txt', 'w')

try:
    file.write ('Hello')
finally:
    file.close ()

### Syntax flexibility

with open ('./file.txt', 'w') as file:
    file.write ('Hello')