#Demonstrate the FillInQuestion class
from questions import FillInQuestion
#create the question and expected answer
q = FillInQuestion()
q.setText("The inventor of Python was _Guido van Rossum_")

#Display the question and obtain user's response
q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))
