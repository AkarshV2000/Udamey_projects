from question_model import Question
from project_data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for ques in question_data:
    question_text = ques['text']
    question_answer = (ques['answer']) 
    new_ques = Question(question_text,question_answer)
    question_bank.append(new_ques)
quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quizz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
