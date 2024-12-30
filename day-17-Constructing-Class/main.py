from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]


#  iterating through question data and creating a question object with each data and saving in list

for item in question_data:
    question_item=Question(item["text"],item["answer"])
    question_bank.append(question_item)

quiz=QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")



