cont='y'
while cont=='y' or cont=='Y':
    def cal(M1,M2,M3,M4,M5):
        t=(M1+M2+M3+M4+M5)
        percen=(t/500)*100
        return t,percen
    #main
    name=input("Enter your name--> ")
    roll=int(input("Enter your Roll no.--> "))
    Class=int(input("Enter your Class--> "))
    phy=float(input("Enter your marks in Physics--> "))
    chem=float(input("Enter your marks in Chemistry--> "))
    math=float(input("Enter your marks in Maths--> "))
    eng=float(input("Enter your marks in English--> "))
    c_s=float(input("Enter your marks in Computer Science--> "))
    dict_marks={"Physics":phy,"Chemistry":chem,"Math":math,"English":eng,"Computer Science":c_s}
    T,per=cal(phy,chem,math,eng,c_s)
    if per>=40:
        Result="Pass"
    elif per<40:
        Result="Fail"
    else:
        print("No result Found")
    print("Sahoday Sr. Sec. School")
    print("Name--> ",name)
    print("Roll no.--> ",roll)
    print("Class--> ",Class)
    print("Marks in 5 Subject--> ",dict_marks)
    print("Total Marks--> ",T)
    print("Percentage--> ",per)
    print("Result--> ",Result)
    cont=input("DO you want to continue y/n? ")
    
    
    
    
    
        









    
