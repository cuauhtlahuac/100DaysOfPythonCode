#
# This file is only for info proposes
#

from question_model import Question
from data import question_data


def build_question_bank():
    new_data_list = []
    for data in question_data:
        new_data_list.append(Question(data['text'], data['answer']))

    return new_data_list


question_bank = build_question_bank()

print(question_bank)
