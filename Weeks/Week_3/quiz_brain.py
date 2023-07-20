class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ") .lower()
        self.check_answer(answer, current_question.answer)
    def still_has_questions(self):
        if self.q_number < len(self.q_list):
            return True
        else: 
            return False
    
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            print("You got it right.")
            self.score += 1
            print(f"Your current score is {self.score}/{self.q_number}")
        else:
            print("That's wrong")
            print(f"Your current score is {self.score}/{self.q_number}")
