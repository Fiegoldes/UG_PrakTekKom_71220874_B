print ("Select_operation")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")
def hitung_angka () :
    p = int (input ("Enter choice (1/2/3/4) :"))
    if p == 1 :
        a = float (input ("Enter first number :"))
        b = float (input ("Enter second number :"))
        w = (a + b)
        print (a, "+" ,b, "=",w)
    elif p == 2 :
        a = float (input ("Enter first number :"))
        b = float (input ("Enter second number :"))
        q = (a - b)
        print (a, "-" ,b, "=",q)
    elif p == 3 :
        a = float (input ("Enter first number :"))
        b = float (input ("Enter second number :"))
        e = (a * b)
        print (a, "*" ,b, "=",e)
    else :
        a = float (input ("Enter first number :"))
        b = float (input ("Enter second number :"))
        r = (a / b)
        print (a, ":" ,b, "=",r)
hitung_angka ()



   