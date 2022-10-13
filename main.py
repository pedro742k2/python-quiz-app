from question_model import Question
from quiz_brain import QuizBrain
from data import questions_data
from ui import QuizInterface
import html

question_bank = []

# Iterate through hard-coded questions array
for question in questions_data:
    # Get question
    question_text = html.unescape(question["question"])
    # Get correct answer
    question_answer = question["correct_answer"]
    # Create a question model
    new_question = Question(question_text, question_answer)
    # Add to the question bank array
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
