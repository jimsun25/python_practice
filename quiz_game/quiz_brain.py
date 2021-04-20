class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        cur_q = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"{self.question_number}. {cur_q.text} True or False: ")
        self.check_answer(user_input, cur_q.answer)

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it~")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer is {c_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
