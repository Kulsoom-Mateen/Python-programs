s1=int(input("Enter marks of English : "))
s2=int(input("Enter marks of Urdu : "))
s3=int(input("Enter marks of Chemistry : "))
s4=int(input("Enter marks of Mathematics : "))
s5=int(input("Enter marks of Physics : "))
s6=int(input("Enter marks of Islamiat : "))
total=550
obt=s1+s2+s3+s4+s5+s6
average=obt/6
per=obt/total*100
print("Total marks : 550")
print("Obtained marks : "+str(obt))
print("Percantage : "+str(per)+" %")
if(per>=80):
    print("Grade : A+")
elif(per<80 and per>=70):
    print("Grade : A")
elif(60<=per<70):
    print("Grade : B")
elif(50<=per<60):
    print("Grade : C")
elif(40<=per<50):
    print("Grade : D")
else:
    print("Fail")