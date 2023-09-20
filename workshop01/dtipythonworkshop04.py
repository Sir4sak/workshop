def InputValue():
    x = float(input("ป้อนเลข : "))
    return x

def FixEquation(x):
    y = 2 * x**2 + 2 * x + 1
    return y

def ShowY(y) :
   print ("แก้สมการได้ ", y, )

x = InputValue ()
y = FixEquation (x)
ShowY(y)
