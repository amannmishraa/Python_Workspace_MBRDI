
class Teacher:
    def __init__(self, name, tid):
        self.name = name
        self.id = tid
        self.students = []  # Association

    def add_student(self, student):
        self.students.append(student)
    def total_strength(self):
        return len(self.students)
    def rusticate_low_marks(self):
        self.students = [s for s in self.students if s.marks >= 20]

    def __str__(self):
        # Sort students by marks in descending order
        sorted_students = sorted(self.students, key=lambda s: s.marks, reverse=True)
        student_list = "\n  ".join(str(s) for s in sorted_students)
        return f"Teacher: {self.name} (ID: {self.id})\nTotal Students: {self.total_strength()}\nStudents:\n  {student_list}"

class Student:
    def __init__(self, name, sid, marks):
        self.name = name
        self.id = sid
        self.marks = marks

    def distinction(self):
        return self.marks >= 75
    def first_division(self):
        return self.marks >= 60
    def second_division(self):
        return self.marks >= 45 and self.marks< 60
    def third_division(self):
        return self.marks >= 35 and self.marks < 45
    def fail(self):
        return self.marks <35

    def __str__(self):
        if self.distinction():
            status = "Distinction"
        elif self.first_division():
            status = "First Division"
        elif self.second_division():
            status = "Second Division"
        elif self.third_division():
            status = "Third Division"
        else:
            status = "Fail"
        return f"Student: {self.name} (ID: {self.id}), Marks: {self.marks}, {status}"


# Create teacher
teacher = Teacher("ABC", 101)

# Create students
student1 = Student("X", 1, 75)
student2 = Student("Y", 2, 15)
student3 = Student("Z", 3, 60)
student4 = Student("A",4,79)

teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)
teacher.add_student(student4)
teacher.rusticate_low_marks()

print(teacher)

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []  # Aggregation

#     def add_book(self, book):
#         self.books.append(book)

#     def __str__(self):
#         book_list = ", ".join(str(book) for book in self.books)
#         return f"Library: {self.name}, Books: [{book_list}]"


# # Create Book objects independently
# b1 = Book("Harry Potter", "J.K. Rowling")
# b2 = Book("The Hobbit", "J.R.R. Tolkien")

# # Create Library object and aggregate books
# lib = Library("City Central")
# lib.add_book(b1)
# lib.add_book(b2)

# print(lib)

# # Delete library
# del lib

# # Books still exist
# print(b1)
# print(b2)
