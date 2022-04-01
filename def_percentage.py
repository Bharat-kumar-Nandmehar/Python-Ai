#This is for calculating % using def function
conti='y'
while conti=='y' or conti=='Y':
   def calculation(Total_marks):
    cal=(Total_marks/500)*100
    return cal
   Pass=40
   name=input("Enter your Name--> ")
   roll=input("Enter your Roll no.--> ")
   Class=input("Enter your Class--> ")
   Physics=float(input("Enter the marks of Physics--> "))
   English=float(input("Enter the marks of English--> "))
   Chemistry=float(input("Enter the marks of Chemistry--> "))
   Maths=float(input("Enter the marks of Maths--> "))
   Computer_science=float(input("Enter the marks of Computer_science--> "))
   marks_list=[Physics,English,Chemistry,Maths,Computer_science]
   Total_marks=sum(marks_list)
   percentage=calculation(Total_marks)
   if percentage>Pass:
      print("Sahoday Sr. Sec. School")
      print("Name--> ",name)
      print("Roll No.--> ",roll)
      print("Class--> ",Class)
      dict_marks={'Physics':Physics,'English':English,'Chemistry':Chemistry,'Maths':Maths,'Computer.science':Computer_science}
      print("Marks in 5 subject--> ",dict_marks)
      print("Total marks--> ",Total_marks)
      print("Percentage--> ",percentage)
      print("Result--> Pass")
   elif percentage<=40:
         print("Sahoday Sr. Sec. School")
         print("Name--> ", name)
         print("Roll No.--> ", roll)
         print("Class--> ", Class)
         dict_marks = {'Physics': Physics, 'English': English, 'Chemistry': Chemistry, 'Maths': Maths,'Computer.science': Computer_science}
         print("Marks in 5 subject--> ", dict_marks)
         print("Total marks--> ", Total_marks)
         print("Percentage--> ", percentage)
         print("Result--> Fail")
   else:
      print("Some error occured , No result found")
   conti=input("If you want to continue press y/Y?")




