maths= int(input("maths: "))
if maths<0 or maths>100:
    print("invalid input")
english=int(input("english: "))
if english<0 or english>100:
    print("invalid input")
kisw=int(input("kiswahili: "))
if kisw<0 or kisw>100:
    print("invalid input")
bio=int(input("biology: "))
if bio<0 or bio>100:
    print("invalid input")
chem=int(input("chemistry: "))
if chem<0 or chem>100:
    print("invalid input")
phy=int(input("physics: "))
if phy<0 or phy>100:
    print("invalid input")

sum=maths+english+kisw+bio+chem+phy
mean=sum/6

print("grade")
if mean>=0 and mean<= 39:
    print("E")
if mean>=40 and mean<=50:
    print("D")
if mean>=51 and mean<=60:
    print("C")
if mean>=61 and mean<=70:
    print("B")
if mean>=71 and mean<=100:
    print("A")















