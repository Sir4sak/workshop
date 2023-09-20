

def InputInfo () : 
    Number = int(input("ป้อนรหัสนักเรียน : "))
    Name = input("ป้อนชื่อนักเรียน : ")
    Grade = float(input("ป้อนเกรดที่ได้ : "))   
    return Number,Name,Grade
def CalGrade (Number,Name,Grade):
    if Grade >=2 : 
        print("ผ่าน ")
    elif Grade < 2 :
        print("ไม่ผ่าน ")


Number,Name,Grade = InputInfo ()
CalGrade (Number,Name,Grade)