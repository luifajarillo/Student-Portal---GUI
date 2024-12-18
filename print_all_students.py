class PrintAllStudents:
    def __init__(self, student):
        self.student_data = student

    def all_students(self):
        students = []
        for x in self.student_data.allstudents:
            students.append(str(x))
        return "\n".join(students)