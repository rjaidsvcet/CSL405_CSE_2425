from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__ == '__main__':
    pass

    # Remove the pass and call the function to perform write.
    # Read the file that was created while writing.
    # Make the changes in the file by appending some material.
    # Again read the same file.

    '''
    Print all the output of the function.
    For better representation, please use jupyter.
    Will also aid in easy maintanence of files for submissions.
    '''