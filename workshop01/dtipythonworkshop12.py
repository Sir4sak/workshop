def InputInfo () : 
    HeadName = input("ป้อนชื่อหัวหน้ากรุ๊ปทัวร์ : ")
    NumberPhone = int(input("ป้อนเบอร์โทรศัพท์ติดต่อกลับของหัวหน้ากรุ๊ปทัวร์ : "))
    Value = int(input("ป้อนจำนวนคนที่จะไปทัวร์ : "))
    return HeadName,NumberPhone,Value 

def calValue (HeadName,NumberPhone,Value):
    if Value <=2 : 
        print("คิดแพ็คเก็จละ 300 บาทต่อคน ")
    elif Value >= 3  and Value <=5:
        print("คิดแพ็คเก็จละ 250 บาทต่อคน ")
    elif Value >= 6  and Value <=10:
        print("คิดแพ็คเก็จละ 210 บาทต่อคน ")
    elif Value >= 11 :
        print("คิดแพ็คเก็จละ 150 บาทต่อคน ")

HeadName,NumberPhone,Value, = InputInfo ()
calValue (HeadName,NumberPhone,Value)