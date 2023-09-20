def InputInfo () : 
    Name = input("ป้อนฃื่อผู้ใช้เบอร์โทรศัพท์ : ")
    Number = int(input("ป้อนเบอร์โทรศัพท์ : "))
    Minute = int(input("ป้อนจำนวนนาทีที่ใช้โทรศัพท์ : "))
    return  Name,Number,Minute

def calValue (Name,Number,Minute):
    if Minute <=15 : 
        print("คิดนาทีละ 5 บาท ")
    elif Minute >= 16  and Minute <=30 :
        print("คิดนาทีละ 3 บาท ")
    elif Minute >= 31 :
        print("คิดนาทีละ 1.50 ")


Name,Number,Minute, = InputInfo ()
calValue (Name,Number,Minute)