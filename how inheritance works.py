class person(object):
    def __init__(self, name):
        self.name = name.upper()
        
class student(person):
    def __init__(self, name, course):
        person.__init__(self, name) # DONT FORGET THIS LINE
        self.course = course
#        self.name = name #if I was to keep this one - OVERWRITES!
      
s = student('ilja', 'biology')
print(s.name)
print(s.course)