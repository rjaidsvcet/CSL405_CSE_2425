class Student:
    def studentName (self, name, surname):
        self.firstname = name
        self.lastname = surname
        return '{} {}'.format (self.firstname, self.lastname)

if __name__ == '__main__':
    # Creating an object 
    firstStudent = Student ()
    print(firstStudent.studentName (name='ABC', surname='DEF'))
