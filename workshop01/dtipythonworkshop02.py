def InputInfo ():
    Name = input ("ชื่อนักเรียน : ")
    Point_1 = int(input ("คะแนนครั้งที่ 1 : "))
    Point_2 = int(input ("คะแนนครั้งที่ 2 : "))
    Point_3 = int(input ("คะแนนครั้งที่ 3 : "))
    return Name,Point_1,Point_2,Point_3

def calAverage (Name,Point_1,Point_2,Point_3):
    AveragePoint = float(Point_1 + Point_2 + Point_3)/3
    print(Name,"มีคะแนนเฉลี่ย" ,AveragePoint )
    
Name,Point_1,Point_2,Point_3 = InputInfo ()
calAverage(Name,Point_1,Point_2,Point_3)