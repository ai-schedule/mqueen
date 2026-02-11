import re

class account:
    def __init__(self):
        self.name=input('enter your name')
        self.uid=int(input('enter yout uids'))
        self.username=input('enter username')
        self.role= input ("enter role(admin/student:)").lower()
        
        while True:
            self.password = input('Enter password: ')
            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
            if re.match(pattern, self.password):
                print("Strong password accepted")
                break
            else:
                print("Weak password!")
        self.marks={}
        self.attendance= None
        print("attendence created succeffully")
        
        print('saved')

    def checker(self):
        self.passw=input('enter password')
        if self.passw==self.password:
            print("Login Successfully")
            return True
        else:
            print('wrong username')
            return False
        
    def add_marks(self):
        if self.role !="admin":
            print("acces denied! only admin can add marks")
            return
        student_username=input("enter the student name")
        student = load_from_file(student_username)
        
        if student is None or student.role!="student":
            print("invalid student.")
        else:
            subject= input("enter the subject:")
            marks=int(input("enter the marks"))
            student.marks[subject]=marks
            save_to_file(student)
            print("marks added/updated successfully")
            
    def view_marks(self):
        if self.role =="admin":
            student_username=input("enter student username:")
            student = load_from_file(student_username)
            if student is None:
                print("student not found")
                return
            if not student.marks:
                print("no marks available")
            else:
                print("marks")
                for subject, marks in self.marks.items():
                    print(subject,":",marks)
        else:
            if not self.marks:
                print("no marks available")
            else:
                print("your marks:")
                for subject,mark in self.marks.items():
                    print(subject,":",marks)
                    
    def average(self):
        if not self.marks:
            print("no marks avaiable")
        else:
            total = sum(self.marks.values())
            count = len(self.marks)
            print("average:",total/count)
            
    def percentage(self):
        if not self.marks:
            print("no marks available")
        else:
            total=sum(self.marks.values())
            max_marks =len(self.marks)*100
            percentage=(total/max_marks)*100
            print("percentage:",percentage,"%")
            
    def add_attendance(self):
        if self.role!="admin":
            print("access denied!only admin")
            
        else:
            student_username=input("enter students username:")
            student=load_from_file(student_username)
            
            if student is None or student.role!="student":
                print("iinvalid student.")
                return
            
            attended=int(input("enter attended classes:"))
            total = int(input("enter the total classes:"))
            student.attendance=(attended,total)
            save_to_file(student)
            print("Attendance added Succesfully")
            
    def view_attendance(self):
        if self.role=="admin":
            student_username= input("enter student username:")
            student = load_from_file(student_username)
            if student is None:
                print("student not found")
                return
            if not student.attendance:
                print("no attendance record")
            else:
                attended, total= student.attendance
                print("attendance:",attended,"/",total)
                precentage=(attended/total)*100
                print("Attendance Percentage:",percentage,"%")
        else:
            if not self.attendance:
                print("no attendence record.")
            else:
                if not self.attendance:
                    print("no attendance record.")
                else:
                    attended, total = self.attendance
                    print ("your attendance:",attended,"/",total)
            
                              
    def view_details(self):
        if self.role == "admin":
            choice=input("""D-For Admin Details\n
d-For Student Details\n
Enter Your Choice !""")
            if choice =="D":
                print("\n-----#ADMIN#-----\n")
                print("Name",self.name)
                print("UID",self.uid)
                print("Username",self.username)
            elif choice =="d":
                student_username = input("enter student username:")
                student = load_from_file(student_username)
                if student is None:
                    print("student not found")
                else:
                    print("\n-----#STUDENT#-----\n")
                    print("name",student.name)
                    print("UID",student.uid)
                    print("Username:",student.username)
            else:
                print ("invalid choice")
        else:
            print("\n-----#YOUR DETAILS#-----\n")
            print("Name",self.name)
            print("UID",self.uid)
            print("Username:",self.username)
            
    

def save_to_file(obj):
    file = obj.username + ".txt"
    with open(file, "w") as f:
        f.write(obj.name + "\n")
        f.write(str(obj.uid) + "\n")
        f.write(obj.username + "\n")
        f.write(obj.password + "\n")
        f.write(obj.role + "\n")

        f.write(str(obj.marks)+"\n")
        
        f.write(str(obj.attendance)+"\n")

def load_from_file(username):
    file = username + ".txt"
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        obj = account.__new__(account)
        obj.name = lines[0].strip()
        obj.uid = int(lines[1].strip())
        obj.username = lines[2].strip()
        obj.password = lines[3].strip()
        obj.role=lines[4].strip()

        obj.marks=eval(lines[5].strip())if len(lines)>5 else {}
        obj.attendance=eval(lines[6].strip())if len(lines)>6 else None
        return obj
    

    except FileNotFoundError:
        return None

while True:
    print("1. New Account")
    print("2. Existing Account")
    print("3. Exit")
    choice = input("Enter Choice: ")

    if choice == "1":
        acc = account()
        save_to_file(acc)

    elif choice == "2":
        uname = input("Enter Username: ")
        acc = load_from_file(uname)

        if acc is None:
            print("Account does not exist")
            continue
        
        if not acc.checker():
            continue

        while True:
            if acc.role =="admin":
                print("\n--- ADMIN PANEL ---")
                print("1.ADD MARKS")
                print("2.VIEW MARKS")
                print("3.PERCENTAGE")
                print("4.ADD ATTENDANCE")
                print("5.VIEW ATTENDANCE")
                print("6.VIEW DETAILS")
                print("7.LOGOUT")

                ch= input("Enter  Your Choice")
                match ch:
                    case "1":
                        acc.add_marks()
                    case "2":
                        acc.view_marks()
                    case "3":
                        acc.percentage()
                    case "4":
                        acc.add_attendance()
                    case "5":
                        acc.view_attendance()
                    case "6":
                        acc.view_details()
                    case "7":
                        print("logging out...")
                        break
                    case _:
                        print("invalid choice")
            else:
                print("\n--- STUDENT PANEL ---")
                print("1.VIEW MARKS")
                print("2.AVERAGE")
                print("3.PERCENTAGE")
                print("4.VIEW ATTENDANCE")
                print("5.VIEW DETAILS")
                print("6.LOGOUT")

                ch =input("Enter Your Choice:")
                match ch:
                    case"1":
                        acc.view_marks()

                    case"2":
                        acc.average()
                    case"3":
                        acc.percentage()
                    case"4":
                        acc.view_attendance()
                    case"5":
                        acc.view_details()
                    case"6":
                        print("logging out...")
                        break
                    case _:
                        print("invalid choice")
    elif choice=="3":
        print("exit ")
        break
    else:
        print("invalid choice")





                

