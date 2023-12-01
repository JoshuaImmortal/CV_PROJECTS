try:
    class Person():
        def __init__(self, Firstname, Surname, Gender, Qualification, Occupation):
            self.Firstname = Firstname
            self.Surname = Surname
            self.Gender = Gender
            self.Qualification = Qualification
            self.Occupation = Occupation
        def firstname(self):
            print(f'His first name is {self.Firstname},')
        def surname(self):
            print(f'His surname is {self.Surname},')
        def fullname(self):
            print(f'Hence his full name of said person is {self.Surname} {self.Firstname},')
        def gender(self):
            print(f'He is {self.Gender},')
        def qualifications(self):
            print(f'my qualifications as at time of this documentation is a {self.Qualification} certification,')
        def occupation(self):
            print(f'my current occupation is {self.Occupation} of Cyclobold group of schools.')

    document = Person('Joel', 'Asta', 'Male', 'PHD', 'Head Of Department')
    document.firstname()
    document.surname()
    document.fullname()
    document.gender()
    document.qualifications()
    document.occupation()


    class Child(Person):
        def __init__(self, Firstname, Surname, CHDfirstname, CHDclass, CHDdescription):
            # super().__init__( Firstname, Surname)
            self.Firstname = Firstname
            self.Surname = Surname
            self.CHDfirstname = CHDfirstname
            self.CHDclass = CHDclass
            self.CHDdescription = CHDdescription
        def chdfirstname(self):
            print(f'The first name of the child is {self.CHDfirstname},')
        def chdsurname(self):
            print(f'The surname of the child is {self.Surname},')
        def chdfullname(self):
            print(f'The fullname of the child is {self.Surname} {self.CHDfirstname},')
        def chdclass(self):
            print(f'The child is currently in {self.CHDclass},')
        def chddescription(self):
            print(f'{self.CHDdescription} Mr. {self.Surname} {self.Firstname}.')

    subdocument = Child('Joel', 'Asta', 'Daniel', 'Primary 4', 'This is the child of')
    subdocument.chdfirstname()
    subdocument.chdfullname()
    subdocument.chdclass()
    subdocument.chddescription()
except Exception as Error:
    print(Error)