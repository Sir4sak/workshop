def InputInfo () : 
    Name = input ("ป้อนชื่อผู้กู้ : ")
    AmountOfMoney = float(input("ป้อนจำนวนเงินกู้ : "))
    return Name,AmountOfMoney

def CalInterest (Name,AmountOfMoney) :
    if AmountOfMoney >= 1000 :
        print ("อัตราดอกเบี้ยเงินกู้ทีจำนวน",AmountOfMoney*(2.5/100))
    elif AmountOfMoney <1000 :
        print ("อัตราดอกเบี้ยเงินกู้ทีจำนวน",AmountOfMoney*(5.5/100))


Name,AmountOfMoney = InputInfo ()
CalInterest (Name,AmountOfMoney)

