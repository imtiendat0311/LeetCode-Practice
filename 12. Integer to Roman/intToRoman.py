def intToRoman(num):
    a=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    b=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    c=[]
    for i in str(num):
        c.insert(0,int(i))
    print(c)

intToRoman(10)