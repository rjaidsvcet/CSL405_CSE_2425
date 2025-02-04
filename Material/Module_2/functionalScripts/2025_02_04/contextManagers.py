class File:
    def __init__ (self, filename, method):
        self.file = open (filename, method)

    def __enter__ (self):
        print ('Enter Method is executed')
        return self.file
    
    def __exit__ (self, type, value, traceback):
        print (f'{type}, {value}, {traceback}')
        print ('Exit method is executed')
        self.file.close ()
        # return True
        if type == Exception:
            return True
        
if __name__ == '__main__':
    with File ('./file.txt', 'w') as f:
        print ('Middle part is executed')
        f.write ('Some generic content')
        raise Exception ()