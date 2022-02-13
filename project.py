#This project is of hotel managemnet
print("Welcome to our Hotel")
ch=int(input("Enter your choice: "))
if ch==1:
    print("Facilities in Room")
    D_A_R=['Double Bed','Full furnished A/C Room','One table' , 'One chair']
    print("",D_A_R)
    book=input("To book this room press yes (y): ")
    if book=="yes" or book=="Yes" or book=="y" or book=="Y":
        '''def Detailsofcustomer(name,email,phone,address):
            customer=Detailsofcustomer
            return customer'''
        print("Rooms available in this hotel for this category is '20' ")
        no_rm_book=int(input("Enter no. of people: "))
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        phone=input("Enter your mobile (number): ")
        address=input("Enter your address: ")
        rm=int(input("Enter No. of rooms you want to register: "))
        #for int in rm:
        avail=20-rm
        print("No. of room availbale now: ",avail)
        print("If you want to change your details press(c) otherwise no further changes will be made \n'If you want to continue press(y)'")
        update = input("To change press(c), continue press(y): ")
        #re_up = "y"
        #while re_up == "yes" or re_up == "Yes" or re_up == "y" or re_up == "Y":
        #update = input("To change press(c), continue press(y): ")

        if update=='c' or update=='C':

                up=[name,email,phone,address]
            #print("",up)
                print("'To change name press(n)'\n 'To change email press(e)'\n 'To change phone press(p)'\n 'To change address press(a)'")
          #  re='y'
            #while re== "yes" or re== "Yes" or re== "y" or re== "Y":
                change=input("To change your details: ")
                if change=='n' or change=='N':
                    up[0]=input("New name: ")
                elif change=='e' or change=='E':
                    up[1]=input("New Email: ")
                elif change=='p' or change=='P':
                    up[2]=input("New phone no.: ")
                elif change=='a' or change=='A':
                    up[3]=input("New address: ")
                else:
                    print("Wrong choice")
                print("",up)
                   # re=input("To make changes again press(y): ")




        #fun=Detailsofcustomer(name,email,phone,address)
       # print("",fun)






