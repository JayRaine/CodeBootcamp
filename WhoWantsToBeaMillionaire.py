# Create a program capable of displaying questions to the user like Who Wants to Be a Millionaire? 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

questions = ["What is the answer to everything?","Who plays cade-6?","What cake does walter mitty make?","Andrew Rea is otherwise known as?","What mug is a moscow mule served in?"]
#C 42, B Nathan Fillion, C Clementine, D Babish, A Copper
answers = ["C","B","C","D","A"] 
bank = 0
name = str(input("Hello and welcome to who wants to be a millionaire! What is your name? "))
print("Thanks",name)
ready = str(input("Are you ready? Y/N ")).upper()
if ready == "Y":
    print("Ok here we go")
    print("Question 1 for £100")
    print(questions[0])
    print("A Money, B Faith, C 42, D Fun")
    q1 = str(input("What is your answer? ")).upper()
    if q1 == answers[0]:
     print("Correct! Adding £100 to the bank")
     bank += 100
     print("The next question is for £1000")
     print(questions[1])
     print("A Huw Jackman, B Nathan Fillion, C Idris Elba, D Chris Hemsworth")
     q2 = str(input("What is your answer? ")).upper()
     if q2 == answers[1]:
        print("Correct! Adding £1000 to the bank!")
        bank += 1000
        print("The next question is for £10000")cleer
        print(questions[2])
        print("A Lemon, B Chocolate, C Clemintine, D Pineapple")
        q3 = str(input("What is your answer? ")).upper()
        if q3 == answers[2]:
           print("Correct! Adding £10000 to the bank!")
           bank += 10000
           print("The next question is for £100000")
           print(questions[3])
           print("A Mast, B Tifu, C Ninja, D Babish")
           q4 = str(input("What is your answer? ")).upper()
           if q4 == answers[3]:
              print("Correct! Adding £100000 to the bank!")
              bank += 100000
              print("This is the last question! It is for £1000000")
              print(questions[4])
              print("A Copper, B Tumbler, C Collins, D French")
              q5 = str(input("What is your answer? ")).upper()
              if q5 == answers[4]:
                 print("That is correct! You have answered all the questions right!")
                 bank += 1000000
                 print("You will be taking home £",bank)
                 print("Thank you for playing!!!")
              else:
                 print("Sorry you were wrong you leave with £",bank)
                 print("Thank you for playing!!!")   
           else:
              print("Sorry you were wrong you leave with £",bank)
              print("Thank you for playing!!!")    
        else:
           print("Sorry you were wrong you leave with £",bank)
           print("Thank you for playing!!!")      
     else:
        print("Sorry you were wrong you leave with £",bank)
    else: 
       print("Sorry you were wrong you leave with £",bank)
       print("Thank you for playing!!!")
else:
   print("Sorry, see you again soon!")


