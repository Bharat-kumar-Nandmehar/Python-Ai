#This project is of hotel managemnet
print("Welcome to our Hotel")
print("Press 1:- To Book Double bed A/C room")
ch=int(input("Enter your choice: "))
if ch==1:
    print("Facilities in Room")
    D_A_R=['Double Bed','Full furnished A/C Room','One table' , 'One chair']
    print("",D_A_R)
    book=input("To book this room press yes (y): ")
    if book=="yes" or book=="Yes" or book=="y" or book=="Y":
        print("Rooms available in this hotel for this category is '20' ")
        no_rm_book=int(input("Enter no. of people: "))
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        phone=input("Enter your mobile (number): ")
        address=input("Enter your address: ")
        rm=int(input("Enter No. of rooms you want to register: "))
        avail=20-rm
        print("No. of room availbale now: ",avail)
        print("If you want to change your details press(c) otherwise no further changes will be made \n'If you want to continue press(y)'")
        update = input("To change press(c), continue press(y): ")
        if update=='c' or update=='C':
            #re='c'
            #while re=='c' or re=='C':
                up=[name,email,phone,address]
                print("'To change name press(n)'\n 'To change email press(e)'\n 'To change phone press(p)'\n 'To change address press(a)'")
                change=input("To change your details: ")
                if change=='n' or change=='N':
                    up[0]=input("New name: ")
                    up=[up[0],email,phone,address]
                    print("New Details: ",up)
                    enter=input("Press enter to update details/to print your receipt: ")
                    if enter=='y' or enter=='Y':
                        print("Thank you for booking your Room")
                        print("Your Details: ", up)
                        print("Your OTP for verification oy your id: ", up[0][0:2] + up[2][4:8])
                elif change=='e' or change=='E':
                    up[1]=input("New Email: ")
                    up = [name, up[1], phone, address]
                    print("New Details: ", up)
                    enter = input("Press enter to update details/to print your receipt: ")
                    if enter == 'y' or enter == 'Y':
                        print("Thank you for booking your Room")
                        print("Your Details: ", up)
                        print("Your OTP for verification oy your id: ", up[0][0:2] + up[2][4:8])
                elif change=='p' or change=='P':
                    up[2]=input("New phone no.: ")
                    up = [name, email,up[2] , address]
                    print("New Details: ", up)
                    enter = input("Press enter to update details/to print your receipt: ")
                    if enter == 'y' or enter == 'Y':
                        print("Thank you for booking your Room")
                        print("Your Details: ", up)
                        print("Your OTP for verification oy your id: ", up[0][0:2] + up[2][4:8])
                elif change=='a' or change=='A':
                    up[3]=input("New address: ")
                    up = [name, email, phone, up[3]]
                    print("New Details: ", up)
                    enter = input("Press enter to update details/to print your receipt: ")
                    if enter == 'y' or enter == 'Y':
                        print("Thank you for booking your Room")
                        print("Your Details: ", up)
                        print("Your OTP for verification oy your id: ", up[0][0:2] + up[2][4:8])
                else:
                    print("Wrong choice")
        elif update=='y' or update=='Y':
            up=(name,email,phone,address)
            print("Thank you for booking your Room")
            print("Your Details: ",up)
            print("Your OTP for verifiation oy your id: ", name[0] + name[1] + phone[3:8])
















