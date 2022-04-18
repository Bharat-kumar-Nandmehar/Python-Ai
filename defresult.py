#def function
cont='y'
while (cont=='y' or cont=='Y'):
    def Cal(M1,M2,M3,M4,M5):
        t=(M1+M2+M3+M4+M5)
        percen=(t/500)*100
        return t,percen

#main
    name=input("Enter your name-->")
    roll=int(input("Enter your Roll no.-->"))
    Class=int(input("Enter your Class-->"))
    phy=float(input("Enter your Physics-->"))
    chem=float(input("Enter your Chemistry-->"))
    eng=float(input("Enter your English-->"))
    math=float(input("Enter your Maths-->"))
    c_s=float(input("Enter your Computer Science-->"))
    T,per=Cal(phy,chem,eng,math,c_s)
    dict_marks={"Physics":phy,"Chemistry":chem,"English":eng,"Maths":math,"Computer Science":c_s}
    if per>=40:
        Result="Pass"
    elif per<40:
        Result="Fail"
    else:
        print("No result Found")

    print("Sahoday Sr. Sec. School")
    print("Name-->",name)
    print("Roll no.-->",roll)
    print("Class-->",Class)
    print("Marks in 5 Subject-->",dict_marks)
    print("Total marks",T)
    print("Percentage",per)
    print("Result",Result)
    cont=input("Do you want to continue y/n?-->")