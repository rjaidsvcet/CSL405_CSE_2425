class Student:
    def __init__ (self, name : str = 'Ned', surname : str = 'Stark'):
        self.firstname = name
        self.lastname = surname
        self.email = name.lower () + '.' + surname.lower () + '@college.edu.in'

    def fullname (self):
        return f'{self.firstname} {self.lastname}'

class Senior (Student):
    def __init__(self, name = 'John', surname = 'Snow', placed : bool = False):
        super ().__init__ (name, surname)
        self.placed = placed


if __name__ == '__main__':
    classStudent = Student ()
    print (classStudent.__dict__)

    childStudent = Senior (placed=True)
    print (childStudent.__dict__)