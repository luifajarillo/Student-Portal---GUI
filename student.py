class StudentInfo:
    def __init__(self):
        self.allstudents = []

    def setFirstName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getFirstName(self):
        return self.name

    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.idnum

    def getEmail(self):
        return self.email

    def getPhoneNum(self):
        return self.phone

    def __str__(self):
        return f"\nName: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone Number: {self.phone}"
        
    def read_data(self):
        with open("student_list.txt", "r") as file:
            line = file.readlines()
            for x in line[0:]:
                linestrip = x.strip().split(",")
                read = StudentInfo()
                read.setFirstName(linestrip[0])
                read.setAge(linestrip[1])
                read.setIDNum(linestrip[2])
                read.setEmail(linestrip[3])
                read.setPhoneNum(linestrip[4])
                self.allstudents.append(read)