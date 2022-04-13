#
# This file is only for info proposes
#

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def build_question_bank():
    new_data_list = []
    for data in question_data:
        new_data_list.append(Question(data['text'], data['answer']))

    return new_data_list


question_bank = build_question_bank()
quiz_brain = QuizBrain(question_bank)

while quiz_brain.quiz_continue:
    quiz_brain.ask_question()
