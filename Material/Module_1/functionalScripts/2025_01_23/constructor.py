class Student:

    attendance = 0.75

    def __init__ (self, name : str = 'Ned', surname : str = 'Stark'):
        self.firstname = name
        self.lastname = surname
        self.email = name.lower () + '.' + surname.lower () + '@college.edu.in'

    def fullname (self):
        return f'{self.firstname} {self.lastname}'
    
if __name__ == '__main__':
    sophomore = Student ('Harry', 'Potter')
    print (sophomore.__dict__)
    senior = Student ('Clark', 'Kent')
    print (senior.__dict__)
    senior.attendance = 0.65
    print (senior.attendance)
    print (sophomore.attendance)
