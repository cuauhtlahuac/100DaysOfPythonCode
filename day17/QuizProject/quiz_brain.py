from random import randint


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.quiz_continue = True

    # asking the questions
    def ask_question(self):
        length = len(self.question_list)
        # checking if we're the end of the quiz
        if length <= 0:
            print("End of the Quiz")
            self.quiz_continue = False
        else:
            index = randint(0, length - 1)
            question = self.question_list[index]
            self.question_list.pop(index)
            user_answer = input(f'{question.text} - please type: True / False. ').capitalize()
            # checking if the answer was correct
            if user_answer == question.answer:
                print("CORRECT")
                return
            print("WRONG!!!")
            return
