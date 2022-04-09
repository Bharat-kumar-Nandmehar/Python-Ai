#This is for calculating Commission

def  cal(S1,S2,S3,S4,S5,S6,S7):
    T=(S1+S2+S3+S4+S5+S6+S7)
    return T
s1=float(input("Enter the sale in day 1:-"))
s2=float(input("Enter the sale in day 2:-"))
s3=float(input("Enter the sale in day 3:-"))
s4=float(input("Enter the sale in day 4:-"))
s5=float(input("Enter the sale in day 5:-"))
s6=float(input("Enter the sale in day 6:-"))
s7=float(input("Enter the sale in day 7:-"))
t=cal(s1,s2,s3,s4,s5,s6,s7)
if t<=10000:
    com = (t * 0.1)
    print("Total Sale in 7 Days:- ",t)
    print("Commission on total Sale in 7 Days:- ",com)
elif t==10000 or t <= 20000:
    com=(t*0.2)
    print("Total Sale in 7 Days:- ", t)
    print("Commission on total Sale in 7 Days:- ", com)
elif t>20000:
    com=(t*0.25)
    print("Total Sale in 7 Days:- ", t)
    print("Commission on total Sale in 7 Days:- ", com)
else:
    print("Error occured")


#Another Method
def  cal(S1,S2,S3,S4,S5,S6,S7):
    T=(S1+S2+S3+S4+S5+S6+S7)
    if T <= 10000:
        com = (T * 0.1)
    elif T == 10000 or T <= 20000:
        com = (T * 0.2)
    elif T > 20000:
        com = (T * 0.25)
    return T,com
s1=float(input("Enter the sale in day 1:-"))
s2=float(input("Enter the sale in day 2:-"))
s3=float(input("Enter the sale in day 3:-"))
s4=float(input("Enter the sale in day 4:-"))
s5=float(input("Enter the sale in day 5:-"))
s6=float(input("Enter the sale in day 6:-"))
s7=float(input("Enter the sale in day 7:-"))
t,comm=cal(s1,s2,s3,s4,s5,s6,s7)
print("Total Sale in 7 Days:- ", t)
print("Commission on total Sale in 7 Days:- ", comm)




