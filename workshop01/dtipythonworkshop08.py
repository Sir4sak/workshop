def InputInfo ():
    Name = input("ป้อนจังหวัด : ")
    Ph = float(input("ป้อนค่า PH : "))
    return Ph,Name,

def CalPh (Ph,Name) :
    if Ph >= 7 and Ph <= 8 :
        print ("Result is Normal ")
    elif Ph > 8 :
        print ("Result is Acid ")
    elif Ph < 7 :
        print ("Result is Alkali ")
    else : 
        print ("Error")
Ph,Name  = InputInfo ()
CalPh(Ph,Name)