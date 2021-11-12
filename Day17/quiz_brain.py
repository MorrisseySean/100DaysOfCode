from data import question_data
from question_model import Question
class QuizBrain: 
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0

    def next_question(self):
        question = self.question_list[self.question_number]        
        self.question_number = self.question_number + 1
        answer = input(f"Q{self.question_number}. {question.text} (True / False): ")
        self.check_answer(answer, question.answer)
    
    def has_more_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Good job!")
            self.user_score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.user_score} / {self.question_number}")
            

