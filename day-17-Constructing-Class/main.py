from question_model import Question
from data import question_data

question_bank=[]


#  iterating through question data and creating a question object with each data and saving in list

for item in question_data:
    question_item=Question(item["text"],item["answer"])
    question_bank.append(question_item)

print(question_bank[0].text)

