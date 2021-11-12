from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
for question in question_data:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
while quiz.has_more_questions():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Your final score is {quiz.user_score} / {quiz.question_number}")