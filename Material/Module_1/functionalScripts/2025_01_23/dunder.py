class Student:

    attendance = 0.75

    def __init__ (self, name : str = 'Ned', surname : str = 'Stark'):
        self.firstname = name
        self.lastname = surname
        self.email = name.lower () + '.' + surname.lower () + '@college.edu.in'

    def fullname (self):
        return f'{self.firstname} {self.lastname}'
    
    def __str__(self):
        return 'String Dunder Method'

    def __repr__(self):
        return f'Firstname : {self.firstname} and Lastname : {self.lastname}'
    
    def __add__ (self):
        return (self.attendance + self.attendance)
    
if __name__ == '__main__':
    firstStudent = Student ()
    print (firstStudent.__add__())
    # print (firstStudent.__repr__())