from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

# for i in range(0, len(question_data)):
#     question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
#
# for i in range(0, len(question_bank)):
#     print(f"{question_bank[i].text}: {question_bank[i].answer}")

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
#
# for i in range(0, len(question_bank)):
#     print(f"{question_bank[i].text}: {question_bank[i].answer}")

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()
    print("\n")
    if not quiz_brain.still_has_question():
        print("You've completed the quiz")
        print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
