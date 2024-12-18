class SearchStudent:
    def __init__(self, studentList):
        self.student_data = studentList

    def search_student(self, searchWord):
        for x in self.student_data.allstudents:
            if x.idnum == searchWord:
                return f"\nStudent found:\n=============== Student Information ===============\n{x}\n\n================= Nothing Follows ================="
        return f"The student with the ID number {searchWord} does not exist."

    def login_check(self, id):
        for x in self.student_data.allstudents:
            if x.idnum == id:
                print(f"\nWelcome, {x.getFirstName()}!\nPlease choose from the following options:")
                return x.getIDNum()
        return False