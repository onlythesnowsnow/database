class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%s' % (self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'a'
        elif self.score >=60:
            return 'b'
        else:
            return 'c'


bart = Student('bart',59)
lisa = Student('lisa',28)
bart.print_score()
lisa.print_score()
bart.get_grade()