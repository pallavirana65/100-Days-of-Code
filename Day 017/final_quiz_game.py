# Day 17 Project - The Quiz Game
# In this project, we practiced creating classes and defining specific attributes and methods that we wanted for
# our Quiz Game. We defined the structure of the questions in the "question_model" module under the class Question.
# Then we defined the attributes and methods of the game in the "quiz_brain" under the class QuizBrain.
# The data module has a list of the 10 questions used in the quiz. These were randomly generated online from the
# Open Trivia Database (opentdb.com) using the API feature.




from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

