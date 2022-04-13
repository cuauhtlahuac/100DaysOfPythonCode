from random import randint


def get_user_answer(question):
    return input(f'{question} - please type: True / False. ').capitalize()


def handle_answer(user_answer=None, correct_answer=None):
    if user_answer == correct_answer:
        print("CORRECT")
        return
    print("WRONG!!!")
    return


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.quiz_continue = True

    def __get_question(self, index):  # double underscore to make a private method
        return self.question_list[index]

    def __delete_question_from_list(self, index):
        self.question_list.pop(index)

    # asking the questions
    def ask_question(self):
        length = len(self.question_list)
        # checking if we're the end of the quiz
        if length <= 0:
            print("End of the Quiz")
            self.quiz_continue = False
        else:
            index = randint(0, length - 1)
            question = self.__get_question(index)
            self.__delete_question_from_list(index)
            user_answer = get_user_answer(question.text)
            # checking if the answer was correct
            handle_answer(user_answer, question.answer)

