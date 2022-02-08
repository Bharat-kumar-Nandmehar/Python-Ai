#Making an Ap using def function
print("Press 1:- To find the value of an:")
print("Press 2:- To find the value of a (first number):")
print("Press 3:- To find the value of n (no. of term):")
print("Press 4:- To find the value of d (common difference):")
print("Press 5:- To find the value of sum of an AP:")
print("Press 6:- To find the value of d in sum of an AP:")
print("Press 7:- To find the value of a in Sn of Ap:")
ch=int(input("Enter your choice:"))
#This is for finding the value of an in an Ap
if ch==1:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="yes" or cont=="Yes":
         def Ap(a, n, d):
               an1 = a + (n - 1) * d
               return an1
         a = int(input("Enter the value of a (first number):"))
         n = int(input("Enter the value of n (no. of terms):"))
         d = int(input("Enter the value of d (common difference):"))
         an = Ap(a, n, d)
         print("The value of Ap:",an)
         cont=input("If you want to continue press y:")
#This is for finding the value of a in an Ap
elif ch==2:
    cont ="y"
    while cont == "y" or cont == "Y" or cont == "yes" or cont == "Yes":
        def Ap(an,n,d):
             var=(n-1)*d
             a1=an-var
             return a1
        an=int(input("Enter the value of an:"))
        n=int(input("Enter the value of n (no. of term):"))
        d=int(input("Enter the value of d(common difference):"))
        a=Ap(an,n,d)
        print("The value of a (first term)",a)
        cont = input("If you want to continue press y:")
#This for finding the value of n in an Ap
elif ch==3:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="Yes" or cont=="yes":
        def Ap(an,a,d):
            n1=(an-a)/d+1
            return n1
        an=int(input("Enter the value of an:"))
        a=int(input("Enter the value of a (first term):"))
        d=int(input("Enter the value of d (common difference):"))
        n=Ap(an,a,d)
        print("The value of n (no. of term)",n)
        cont=input("If you want to continue press y:")
#This for finding the value of d in an Ap
elif ch==4:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="Yes" or cont=="yes":
        def Ap(an,a,n):
            var1=n-1
            d1=(an-a)/var1
            return d1
        an=int(input("Enter the value of an:"))
        a=int(input("Enter the value of a (first term):"))
        n=int(input("Enter the value of n (no. of terms):"))
        d=Ap(an,a,n)
        print("The value of d (common difference):",d)
        cont=input("If you want to continue press y:")
# This is for finding the sum of Ap
elif ch==5:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="Yes" or cont=="yes":
        def Sn(a,n,d):
            sp1=(n/2)*((2*a)+(n-1)*d)
            return sp1
        a=int(input("Enter the value of a(first term):"))
        n=int(input("Enter the value of n (no. of terms):"))
        d=int(input("Enter the value of d (common difference):"))
        sn=Sn(a,n,d)
        print("The value of sum of an Ap:",sn)
        cont=input("If you want to continue press y:")
# This is for finding the value of d in an Sn of Ap
elif ch==6:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="Yes" or cont=="yes":
        def Sn(sn,a,n):
            var1=2*a
            var2=n-1
            var3=n/2
            d2=((sn/var3)-var1)/var2
            return d2
        sn=int(input("Enter the value of Sn:"))
        a=int(input("Enter the value of a (first term):"))
        n=int(input("Enter the value of n (no. of terms):"))
        d=Sn(sn,a,n)
        print("The value of d in Sum of an Ap:",d)
        cont=input("If you want to continue press y:")
#This is for finding the value of a in Sn of AP
elif ch==7:
    cont="y"
    while cont=="y" or cont=="Y" or cont=="yes" or cont=="Yes":
        def Sn(sn,n,d):
            var=n/2
            var2=(n-1)*d
            a2=((sn/var)-var2)/2
            return a2
        sn=int(input("Enter the value of Sn:"))
        n=int(input("Enter the value of n (no. of terms):"))
        d=int(input("Enter the value of d (common difference):"))
        a=Sn(sn,n,d)
        print("The value of a in Sn of Ap:",a)
        cont=input("If you want to continue press y:")




