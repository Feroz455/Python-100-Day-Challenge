from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
quit = QuizBrain(question_bank)

while  quit.has_question():
    quit.next_question()

print(f"Your score is {quit.correct}/{len(quit.question_list)}")