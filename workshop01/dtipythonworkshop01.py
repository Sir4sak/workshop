def InputNamePrice () :
    Name = input ("ป้อนชื่อสินค้า : ")
    Price = float(input("ป้อนราคา : "))
    return Name,Price
def CalPrice (Name,Price) :
    print(f"{Name} ราคาขายสินค้า {float(Price+(Price*10/100))} ")

Name,Price = InputNamePrice()
CalPrice(Name,Price)