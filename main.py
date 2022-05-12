from data import question_data
from question_model import Question
from quiz_brain import QuizB


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizB(question_bank)
while quiz.still_has_questions():
    quiz.next_question()