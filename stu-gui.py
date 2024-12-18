from tkinter import *
from functools import partial
from student import StudentInfo
from add_student import AddStudent
from searchStudent import SearchStudent
from print_all_students import PrintAllStudents
from login import Login
from tkinter.scrolledtext import *

studentList = StudentInfo()
studentList.read_data()
newStud = AddStudent(studentList)
printInfo = SearchStudent(studentList)
allStudents = PrintAllStudents(studentList)
login1 = Login(studentList)
win = Tk()
btns = []

def login():
    global userID
    userID = login_input.get()
    isloggedin = printInfo.login_check(userID)
    if isloggedin != False:
        login_input.delete(0, 'end')
        login_frame.pack_forget()
        menu_contain.pack(side = "left", fill = "y")
        menu_contain2.pack(fill = "both", expand = True)
        with open("student_list.txt", "r") as file:
            line = file.readlines()
            for students in line:
                linestrip = students.strip().split(",")
                if linestrip[2] == userID:
                    studentList.setFirstName(linestrip[0])
            welcome_label.config(text = f"Welcome to the Student Portal, {studentList.getFirstName()}!")
    else:
        error_login.config(text = "Invalid ID, please try again.", bg = "#F4D9D0", pady = 5)
def view_yours():
    menu_contain2.pack_forget()
    others_bg.pack_forget()
    register_bg.pack_forget()
    all_bg.pack_forget()
    search_input.delete(0, 'end')
    info_frame.place_forget()
    error_label.config(text = " ")
    yours_bg.pack(fill = "both", expand = True)
    label_frame.place(x = 170, y = 250)
    for student in studentList.allstudents:
        if userID == student.idnum:
            yours_info.config(text = student)
def view_others():
    menu_contain2.pack_forget()
    yours_bg.pack_forget()
    register_bg.pack_forget()
    all_bg.pack_forget()
    error_label.config(text = " ")
    others_bg.pack(fill = "both", expand = True)
    search_frame.place(x = 210, y = 200)
def other_students():
    info_frame.place(x = 170, y = 350)
    search_id = search_input.get()
    itexists = printInfo.login_check(search_id)
    if itexists != False:
        for student in studentList.allstudents:
            if search_id == student.idnum:
                info_frame.config(borderwidth = 2)
                others_info.config(text = student, bg = "#fceffa", pady = 5)
    else:
        others_info.config(text = "ID Number does not exists.")
def register():
    menu_contain2.pack_forget()
    yours_bg.pack_forget()
    others_bg.pack_forget()
    all_bg.pack_forget()
    register_bg.pack(fill = "both", expand = True)
    search_input.delete(0, 'end')
    info_frame.place_forget()
def register_newStudent():
    valid = True
    error_message = ""
    for i, entry in enumerate(entries):
        if not entry.get().strip():
            valid = False
            error_message += f"{requirements[i]} field cannot be empty.\n"
            entry.config(bg="#ffcccc")
        else:
            entry.config(bg="white")
    if not valid:
        error_label.config(text = error_message)
    else:
        error_label.config(text = "Student registered successfully!")
        newStud.new_student(entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get())
        for entry in entries: 
            entry.delete(0, 'end')
def show_list():
    menu_contain2.pack_forget()
    yours_bg.pack_forget()
    others_bg.pack_forget()
    register_bg.pack_forget()
    error_label.config(text = " ")
    search_input.delete(0, 'end')
    info_frame.place_forget()
    all_bg.pack(fill = "both", expand = True)
    list_frame.place(x = 120, y = 150)
    global students_info
    students_info = ScrolledText(list_frame, font = ("Century Gothic", 18), width = 45, height = 15, fg = "black", bg = "#fceffa", pady = 10, padx = 10)
    students_info.insert(INSERT, allStudents.all_students())
    students_info.config(state = "disabled")
    students_info.pack()
def logout():
    menu_contain.pack_forget()
    menu_contain2.pack_forget()
    yours_bg.pack_forget()
    others_bg.pack_forget()
    register_bg.pack_forget()
    all_bg.pack_forget()
    students_info.pack_forget()
    search_input.delete(0, 'end')
    info_frame.place_forget()
    login_frame.pack(fill = "both", expand = True)

# Login Page
login_frame = Frame(win, bg = "#1A1A1D")
login_frame.pack(fill = "both", expand = True)
float_frame = Frame(login_frame, bg = "#A64D79", padx = 40, pady = 40, relief = "solid")
float_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
Label(float_frame, text = "Login to Continue", fg = "white", bg = "#3B1C32", width = 15, font = ("Century Gothic", 20), padx = 30, pady = 5).pack()
Label(float_frame, text = "Please enter your ID", fg = "white", bg = "#3B1C32", width = 30, font = ("Century Gothic", 10), padx = 30, pady = 5).pack()
login_input = Entry(float_frame, font = ("Century Gothic", 20))
login_input.pack(padx = 30, pady = 20)
login_btn = Button(float_frame, text = "Login", width = 15, bg = "#F4D9D0", font = ("Century Gothic", 15), command = login)
login_btn.pack()
exit_btn = Button(float_frame, text = "Exit", width = 15, bg = "#F4D9D0", font = ("Century Gothic", 15), command = win.destroy)
exit_btn.pack()
error_login = Label(float_frame, text = "", font = ("Century Gothic", 15), bg = "#A64D79", fg = "red")
error_login.pack()

# View own info
yours_bg = Frame(win, borderwidth = 1, bg = "#A64D79", relief = "sunken")
label_frame = Frame(yours_bg, borderwidth = 3, bg = "#fceffa", relief = "sunken", width = 10)
Label(label_frame, text = "Your Information:", font = ("Century Gothic", 25), fg = "#3B1C32", bg = "#fceffa").pack()
yours_info = Label(label_frame, text = "", font = ("Century Gothic", 20), width = 30, fg = "black", bg = "#fceffa", pady = 10, padx = 10)
yours_info.pack()

# View others
others_bg = Frame(win, borderwidth = 1, bg = "#A64D79", relief = "sunken")
search_frame = Frame(others_bg, bg = "#fceffa", relief = "sunken", padx = 20, pady = 20)
Label(search_frame, text = "Enter an ID Number:", font = ("Century Gothic", 20), fg = "#3B1C32", bg = "#fceffa", padx = 40, pady = 5).pack()
search_input = Entry(search_frame, font = ("Century Gothic", 20), width = 20)
search_input.pack(side = LEFT)
search_btn = Button(search_frame, text = "Search", anchor = "center", font = ("Century Gothic", 15), bg = "#F4D9D0", command = other_students)
search_btn.pack(side = RIGHT)
info_frame = Frame(others_bg, bg = "#A64D79", relief = "sunken", padx = 5)
info_frame.place(x = 170, y = 350)
others_info = Label(info_frame, text = "", width = 30, font = ("Century Gothic", 20), fg = "black", bg = "#A64D79", padx = 10)
others_info.pack()

# Register
requirements = ["Name:", "Age:", "ID Number:", "Email:", "Phone Number:"]
register_bg = Frame(win, borderwidth = 1, bg = "#A64D79", relief = "sunken")
form_frame = Frame(register_bg, bg = "#fceffa", relief = "sunken", padx = 20, pady = 20)
form_frame.place(x = 150, y = 250)
for x in range(len(requirements)):
    Label(form_frame, text = requirements[x], font = ("Century Gothic", 20), justify = "right", bg = "#fceffa", padx = 10).grid(row = x, column = 0, sticky = E)
entries = []
for x in range(len(requirements)):
    new_entry = Entry(form_frame, font = ("Century Gothic", 20), width = 20)
    new_entry.grid(row = x, column = 1)
    entries.append(new_entry)
register_btn = Button(form_frame, text = "Register", anchor = "center", font = ("Century Gothic", 15), bg = "#F4D9D0", command = register_newStudent)
register_btn.grid(row = 6, column = 1, pady = 20)
error_label = Label(form_frame, text = "", font = ("Century Gothic", 20), bg = "#fceffa", padx = 10)
error_label.grid(row = 7, column = 0, columnspan = 2)

# Show all
all_bg = Frame(win, borderwidth = 1, bg = "#A64D79", relief = "sunken")
list_frame = Frame(all_bg, bg = "#fceffa", relief = "sunken", pady = 10, padx = 5)
Label(list_frame, text = "Students:", font = ("Century Gothic", 25), fg = "#3B1C32", bg = "#fceffa").pack()

btn_txt = ["VIEW YOUR INFORMATION", "VIEW OTHER STUDENT'S INFORMATION", "REGISTER A NEW STUDENT", "SHOW STUDENT LIST", "LOGOUT"]
func = [view_yours, view_others, register, show_list, logout]

win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
menu_contain = Frame(win, borderwidth = 1, bg = "#3B1C32", relief = "sunken")
menu_contain2 = Frame(win, borderwidth = 1, bg = "#A64D79", relief = "sunken")

# Buttons
Label(menu_contain, text = "Main Menu", font = ("Century Gothic", 30), fg = "white", bg = "#3B1C32", padx = 20, pady = 38).grid(row = 0, column = 0)
for i, txt in enumerate(btn_txt): 
    btns.append(Button(menu_contain, anchor = "center", width = 35, text = btn_txt[i], font = ("Century Gothic", 15), pady = 48, bg = "#fceffa", fg = "#3B1C32"))
for i in range(len(btns)):
    btns[i].grid(row = i+1, column = 0)
for i in range(len(btns)):
    btns[i].config(command = partial(func[i]))

# Welcome Frame
welcome_frame = Frame(menu_contain2, bg = "#A64D79", padx = 20)
welcome_frame.pack(pady = 350)
welcome_label = Label(welcome_frame, text = "", font = ("Century Gothic", 25), fg = "#fceffa", bg = "#A64D79", padx = 20)
welcome_label.pack()

win.mainloop()