from random import randint

# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    # asking the questions
    def ask_question(self):
        number = randint(0, len(self.question_list))
        question = self.question_list[number]

        self.question_list.pop(number)
        user_answer = input(f'{question.text} - please type: True / False. ').capitalize()

        if user_answer == question.answer:
            print("CORRECT")
            return
        print("WRONG!!!")
        return
