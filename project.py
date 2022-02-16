#This project is of hotel managemnet
print("Welcome to our Hotel")
print("Press 1:- To Book Double bed A/C room")
print("Press 2:- To Book Single bed A/C room")
print("Press 1:- To Book Double bed W/o AC room")
print("Press 1:- To Book Single bed W/o AC room")
ch=int(input("Enter your choice: "))
if ch==1:
    # Double A/C Room
    list= ['Double Bed', 'Double A/C', 'Table', 'Chair']
    print("Facilities in room", list)
    price = 4000
    room = 20
    print("Price of this room/per day: ", price)
    re = 'y'
    while re == 'y' or re == 'Y':
        choice = input("IF you want to book this Room press(y): ")
        if choice == 'y' or choice == 'Y':
            days = int(input("No. of Days you want to stay: "))
            name = input("Enter your Name: ")
            phone = int(input("Enter you Phone no. "))
            email = input("Enter your email: ")
            register = int(input("No. of rooms you want to register: "))
            cost = (price * days) * register
            details = [name, phone, email]
            otp = name[0:2] + email[3:7]
            print("Thank you for registering your room:- ")
            print("Your Details:- ", details)
            print("No. of days want to stay:- ", days)
            print("No of Rooms booked:- ", register)
            print("Room cost to pay:- ", cost)
            print("Your OTP for check-in:- ", otp)
            print("Room available now:- ", (20 - register))
            re = input("If want to register again press(y): ")
elif ch==2:
   # single A/C Room
   list=['Single Bed','Single A/C','Table','Chair']
   print("Facilities in room",list)
   price=2500
   room=20
   print("Price of this room/per day: ",price)
   re='y'
   while re=='y' or re=='Y':
       choice=input("IF you want to book this Room press(y): ")
       if choice=='y' or choice=='Y':
          days=int(input("No. of Days you want to stay: "))
          name=input("Enter your Name: ")
          phone=int(input("Enter you Phone no. "))
          email=input("Enter your email: ")
          register=int(input("No. of rooms you want to register: "))
          cost=(price*days)*register
          details=[name,phone,email]
          otp=name[0:2]+email[3:7]
          print("Thank you for registering your room:- ")
          print("Your Details:- ",details)
          print("No. of days want to stay:- ",days)
          print("No of Rooms booked:- ",register)
          print("Room cost to pay:- ",cost)
          print("Your OTP for check-in:- ",otp)
          print("Room available now:- ",(20-register))
          re=input("If want to register again press(y): ")
elif ch==3:
    # Double W/o AC Room
    list = ['Double Bed','Table', 'Chair']
    print("Facilities in room", list)
    price = 3000
    room = 20
    print("Price of this room/per day: ", price)
    re = 'y'
    while re == 'y' or re == 'Y':
        choice = input("IF you want to book this Room press(y): ")
        if choice == 'y' or choice == 'Y':
            days = int(input("No. of Days you want to stay: "))
            name = input("Enter your Name: ")
            phone = int(input("Enter you Phone no. "))
            email = input("Enter your email: ")
            register = int(input("No. of rooms you want to register: "))
            cost = (price * days) * register
            details = [name, phone, email]
            otp = name[0:2] + email[3:7]
            print("Thank you for registering your room:- ")
            print("Your Details:- ", details)
            print("No. of days want to stay:- ", days)
            print("No of Rooms booked:- ", register)
            print("Room cost to pay:- ", cost)
            print("Your OTP for check-in:- ", otp)
            print("Room available now:- ", (20 - register))
            re = input("If want to register again press(y): ")
elif ch==4:
    # single W/o AC Room
    list= ['Single Bed', 'Table', 'Chair']
    print("Facilities in room", list)
    price = 2000
    room = 20
    print("Price of this room/per day: ", price)
    re = 'y'
    while re == 'y' or re == 'Y':
        choice = input("IF you want to book this Room press(y): ")
        if choice == 'y' or choice == 'Y':
            days = int(input("No. of Days you want to stay: "))
            name = input("Enter your Name: ")
            phone = int(input("Enter you Phone no. "))
            email = input("Enter your email: ")
            register = int(input("No. of rooms you want to register: "))
            cost = (price * days) * register
            details = [name, phone, email]
            otp = name[0:2] + email[3:7]
            print("Thank you for registering your room:- ")
            print("Your Details:- ", details)
            print("No. of days want to stay:- ", days)
            print("No of Rooms booked:- ", register)
            print("Room cost to pay:- ", cost)
            print("Your OTP for check-in:- ", otp)
            print("Room available now:- ", (20 - register))
            re = input("If want to register again press(y): ")
else:
    print("Wrong choice")






























