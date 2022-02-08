#Sum of AP #(an of an AP)
print("Press 1:-- To do sum of an AP")
print("Press 2:-- To do find (an)^th term of an AP")
print("Press 3:-- To find the (N)^th term of an AP")
print("Press 4:-- To find the a (First term) of an AP")
print("Press 5:-- To find the d (common difference) of an AP")
print("Press 6:-- To find Sum of AP using a , n , an")
print("Press 7:-- To find Sn1/Sn2=an1/an2 ,Then find the ratio of their n terms")
ch=int(input("Entre your choice:--"))
if ch==1:
    cont="y"
    while cont=='y' or cont=='Y' or cont=='Yes' or cont=='yes':
        A=int(input("Enter the value of a (First term):--"))
        D=int(input("Enter the value of d (common difference):--"))
        N=int(input("Enter the value of n (Number of term):--"))
        SuAP=(N/2)*(2*A+(N-1)*D)
        print("The sum of AP is:--",SuAP)
        cont=input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==2:
    conti = "y"
    while conti == 'y' or conti == 'Y' or conti == 'Yes' or conti == 'yes':
        A = int(input("Enter the value of a (First term):--"))
        D = int(input("Enter the value of d (common difference):--"))
        N = int(input("Enter the value of n (Number of term):--"))
        AnAP = A + (N - 1) * D
        print("The (an)^th of AP is:--", AnAP)
        conti = input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==3:
    contin = "y"
    while contin == 'y' or contin == 'Y' or contin == 'Yes' or contin == 'yes':
        A = int(input("Enter the value of a (First term):--"))
        D = int(input("Enter the value of d (common difference):--"))
        an = int(input("Enter the value of an (an^)th term of AP:--"))
        N = (an-A)/D+1
        print("The (n)^th term of an AP is:--",N)
        contin = input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==4:
    continu = "y"
    while continu == 'y' or continu == 'Y' or continu == 'Yes' or continu == 'yes':
        an = int(input("Enter the value of an (an)^th term of AP:--"))
        D = int(input("Enter the value of d (common difference):--"))
        N = int(input("Enter the value of n (Number of term):--"))
        T=(N-1)*D
        A=an-T
        print("The vale of a (First term) of an AP is:--",A)
        continu = input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==5:
    cont = "y"
    while cont == 'y' or cont == 'Y' or cont == 'Yes' or cont == 'yes':
        A = int(input("Enter the value of a (First term):--"))
        an = int(input("Enter the value of an (an)^th term of an AP:--"))
        N = int(input("Enter the value of n (Number of term):--"))
        a=an-A
        t=N-1
        D =a/t
        print("The d (common difference)of AP is:--",D)
        cont = input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==6:
    cont = "y"
    while cont == 'y' or cont == 'Y' or cont == 'Yes' or cont == 'yes':
        A = int(input("Enter the value of a (First term):--"))
        an= int(input("Enter the value of an (Last term):--"))
        N = int(input("Enter the value of n (Number of term):--"))
        SuAP = (N/2)*(A+an)
        print("The sum of AP is:--", SuAP)
        cont = input("If you want to continue press Y or y and if you don't want to continue press enter:--")
elif ch==7:
    pass