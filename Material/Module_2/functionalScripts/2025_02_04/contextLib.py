from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    print ('Enter Method')
    file = open (filename, method)
    yield file
    file.close ()
    print ('Exit')

if __name__ == '__main__':
    with genericFileFunction ('./file.txt', 'w') as f:
        print ('Middle')
        f.write ('Hello from the function')