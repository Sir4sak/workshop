def InputInfo():
    Name = input("ป้อนชื่อสินค้า : ")
    Price = float(input("ป้อนราคาสินค้า : "))
    return Name,Price

    
def showScoreStudent(Name,Price):
    print("ชื่อสินค้า",Name,"ราคาสินค้า",Price,"ราคาภาษีของสินค้า",Price*(7/100) )

Name,Price = InputInfo()
showScoreStudent(Name,Price)