# Create a class Student with the following attributes: 
# name (str) 
# marks (list of integers) 
# Overload the following comparison operators to compare students based on their average marks: __gt__: Greater than. 
# __lt__: Less than. 
# __eq__: Equal to.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    def average_marks(self):
        return sum(self.marks) / len(self.marks)  
    
    
    def __gt__(self, other):
        return self.average_marks() > other.average_marks()
   
    def __lt__(self, other):
        return self.average_marks() < other.average_marks()

    def __eq__(self, other):
        return self.average_marks() == other.average_marks()

s1 = Student("Alice", [85, 90, 80])
s2 = Student("Bob", [75, 80, 85])
s3 = Student("Charlie", [85, 90, 80])  


print("s1>s2:",s1 > s2)   
print("s1 < s2:",s1 < s2)   
print("s1 == s3:",s1 == s3)  