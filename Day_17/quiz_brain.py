class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {self.question_list[self.question_number - 1].text} (True/False): ").lower()
        correct_answer = self.question_list[self.question_number - 1].answer
        self.check_answer(user_answer, correct_answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry! That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

