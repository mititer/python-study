class Student:
    '''
    Memeber fields should be firstly defined in __init__()
    '''
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.gpa = gpa
        self.major = major
        self.is_on_probation = is_on_probation
        return
    '''
    Define output for print
    '''
    def __str__(self):
        return "{" + self.name + ", " + self.major + ", " + str(self.gpa) + ", " + str(self.is_on_probation) + "}"

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
