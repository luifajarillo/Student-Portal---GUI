from student import StudentInfo

class AddStudent:
    def __init__(self, studentList):
        self.student_data = studentList

    def add_student(self, newStudent):
        self.student_data.allstudents.append(newStudent)
        with open("student_list.txt", "a+") as file:
            a = newStudent.getFirstName()
            b = newStudent.getAge()
            c = newStudent.getIDNum()
            d = newStudent.getEmail()
            e = newStudent.getPhoneNum()
            file.write(f"{a},{b},{c},{d},{e}")
            file.write("\n")
        file.close

    def new_student(self, name, age, idnum, email, phone):
        newStudent = StudentInfo()
        newStudent.setFirstName(name)
        newStudent.setAge(age)
        newStudent.setIDNum(idnum)
        newStudent.setEmail(email)
        newStudent.setPhoneNum(phone)
        self.add_student(newStudent)