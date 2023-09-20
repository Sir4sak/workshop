def InputInfo () : 
    Number = input ("ป้อนรหัสพนักงาน : ")
    Name = input("ป้อนชื่อพนักงาน : ")
    Salary = float(input("ป้อนเงินเดือนพนักงาน : "))
    return Number,Salary,Name

def CalSalary (Number,Salary,Name) :
    print (Number,Name,"ได้เงินเดือนสุทธิ",Salary-(Salary*7/100)-500 )


Number,Salary,Name = InputInfo ()
CalSalary (Number,Salary,Name)