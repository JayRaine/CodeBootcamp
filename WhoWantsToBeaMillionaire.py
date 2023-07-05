# Create a program capable of displaying questions to the user like Who Wants to Be a Millionaire? 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.
question = "What is the answer to everything?"
print(question)
choices = ["A Money","B Faith","C 42","D Fun"]
print(choices)
a = str(input("What is your answer? "))
print(a)
if (a=="C" or a=="42"):
    print("That is corrrect! The answer to everything is 42!")
else: print("Sorry that is not correct!")

