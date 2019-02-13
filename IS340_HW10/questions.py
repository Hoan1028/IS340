#This module defines a hierarchy of classes that model exam questions.
#A question with a text and answer
class Question:
        #constructs a question with empty question and answer strings
        def __init__(self):
                self._text = ""
                self._answer = ""

        #sets the question string
        def setText(self, questionText):
                self._text = questionText
        #sets the answer string
        def setAnswer(self,correctResponse):
                self._answer = correctResponse
        #checks user response, ignore case and spaces
        def checkAnswer(self,response):
                return response.lower().replace(" ","") == self._answer.lower().replace(" ","")
        #displays the question
        def display(self):
                print(self._text)

#subclass inherits Question
class FillInQuestion(Question):
        #initialize constructor
	def __init__(self):
		Question.__init__(self)
	#split text and answer from string, then assign to separate variables	
	def setText(self,text):
                #create a list of two elements split by '_'; text and answer
		textlist = text.split("_")
		#replace answer by concatinate blank space
		#assign split elements to variables
		self._text = textlist[0] + "__________"
		self._answer = textlist[1]
	#displays the question
	def display(self):
                print(self._text)
