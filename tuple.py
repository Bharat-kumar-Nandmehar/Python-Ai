import math
#from math import ceil

#This is for tuples

#a=(1,2,3,1,434,34,1,2242,1,343,12)
#b=sorted(a) #This will sort the tuple
#print("",b)
#sorted(a) #This will also sort the tuple
#print("",a)
#b=min(a) #This will give the minimum value of tuple a
#print("",b)
#b=max(a) #This will give you the maximum value of tuple a
#print("",b)
#b=sum(a) #This will give you the sum of all value of tuple a (but in nested tuple it throws error)
#print("",b)
#b=a.index(2) #This will tell at index 1 , 2 is present
#print("",b)
#b=a.count(1) #This is will tell you that how many times 1 come in this tuple
#print("",b)
#Tuple to list then list to tuple
'''a=(1,2,"Good","Hello")
print("",a)
print("",type(a))
lst=list(a)
lst[1]=3000
print("",lst)
print("",type(lst))
a=tuple(lst)
print("",a)
print("",type(a))'''
#print(math.ceil(2.03))
#print(math.floor(2.03))
'''NEW={}
X=["AMIT","LALIT","SUMIT","RACHIT"]
for i in range(1,5):
    NEW[i]=X[i-1]
print(NEW)'''
'''Fruits={"orange":15, "banana":12,"mango":8}
Fruits.popitem()
print("",Fruits)
Fruits["mango"] =10+8
print(Fruits)
Fruits["apples"] = 10
print(Fruits)'''
'''a=(eval(input("Enter the number")))
b=(eval(input("Enter the number")))
c=tuple(a)
d=tuple(b)
print("c",c,"d",d)
(c,d)=(d,c)
print("c",c,"d",d)'''
'''def root(a,b,c):
    D=(b**2)-(4*a*c)
    if D>0:
        root1=(-b)+math.pow(D,1/2)/2*a
        root2 =(-b)-math.pow(D, 1 / 2)/ 2 * a
        return (root1,root2)
    elif D==0:
        root=-b/2*a
        root_1=root
        return (root,root_1)
    else:
        print("No real roots")
def v_o_c(r,h):
    return math.pi*r*r*h
a=v_o_c(2,2)
print("",a)'''

'''tupl=eval(input("Enter a tuple:"))
a,b=tupl
tupl=b,a
print("",tupl)'''


'''ch=int(input("Enter:"))
lis=[1,2,34,34,2232,12312,1]
if ch==1:
    a=min(lis)
    print("min", a)
    b=max(lis)
    print("max",b)
elif ch==2:
    c=int(input("number:"))
    d=lis.count(c)
    print("",d)
else:
    print("Wrong choice")'''
# l1=[10,20,30]
# l2=[40,50,60,70]
# print(l1*2)
# print(l1+l2)
#
# rate=500
# quantity=int(input("enter the quantity:"))
# if quantity>=50:
#     discount=(quantity*rate)*20/100
#     print("",discount)


