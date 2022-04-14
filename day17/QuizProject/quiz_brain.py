from random import randint


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.corrects_number = 0
        self.question_list = question_list
        self.quiz_continue = True

    def __handle_answer(self, user_answer=None, correct_answer=None):
        if user_answer == correct_answer:
            print("CORRECT")
            self.corrects_number += 1
        else:
            print("WRONG!!!")
        print(f"Your current score is: {self.corrects_number}/{self.question_number}")

    def __get_user_answer(self, question):
        self.question_number += 1
        return input(f'Q.{self.question_number}: {question} (True/False): ').capitalize()

    def __get_question(self, index):  # double underscore to make a private method
        return self.question_list[index]

    def __delete_question_from_list(self, index):
        self.question_list.pop(index)

    # asking the questions
    def ask_question(self):
        length = len(self.question_list)
        # checking if we're the end of the quiz
        if length <= 0:
            print("End of the Quiz 🏁")
            print(f"Your final score is: {self.corrects_number} / {self.question_number}")
            self.quiz_continue = False
        else:
            index = randint(0, length - 1)
            question = self.__get_question(index)
            self.__delete_question_from_list(index)
            user_answer = self.__get_user_answer(question.text)
            # checking if the answer was correct
            self.__handle_answer(user_answer, question.answer)
