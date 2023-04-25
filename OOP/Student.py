class Student:
    
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade # %0 -100
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
    def get_grade(self):
        return self.grade
    
    def set_grade(self, age):
        self.age = age
        
    
class Course:
        
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
            
        #Attributes
        self.students = []
        self.is_active = False
        
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        
        return (value / len(self.students))
        
        

s1 = Student("John" , 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jack", 19 ,82)

course = Course("Math", 2)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.add_student(s3))
print(course.get_average_grade())

