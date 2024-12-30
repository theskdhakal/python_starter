class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0



    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number +=1
        user_answer=input(f"Q.N.{self.question_number}:{current_question.text } : ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):

        return len(self.question_list) > self.question_number

        # if len(self.question_list) > self.question_number :
        #     return True
        # else:
        #     return False

    def check_answer(self,user_answer,  correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score +=1
            print(f"You got it right. Your score is {self.score}/{self.question_number}")
        else:
            print(f"Oops! Thats's wrong . Your score is {self.score}/{self.question_number}")

        print(f'The correct answer is {correct_answer}')
        print("\n")





