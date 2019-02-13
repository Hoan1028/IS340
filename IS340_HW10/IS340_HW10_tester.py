from questions import Question 


q = Question()

q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")

q.display()
response = input("Your answer: ")
print(q.checkAnswer(response))
