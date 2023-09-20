def InputInfo ():
    yearclass = int(input("ป้อนชั้นปีนักศึกษา : "))
    return yearclass

def Calyearclass (yearclass):
    if yearclass ==1 :
        print ("Welcome Freshman")
    elif yearclass ==2:
        print ("Welcome Sophomore")
    elif yearclass ==3 :
        print ("Welcome Junior")
    elif yearclass ==4 :
        print ("Welcome Senior")    
    else :
        print ("Error")
yearclass = InputInfo ()    
Calyearclass (yearclass)