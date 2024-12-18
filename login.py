class Login:
    def __init__(self, student):
        self.student_data = student

    def login(self, idnum):
        for student in self.student_data.allstudents:
            if idnum == student.idnum:
                return True