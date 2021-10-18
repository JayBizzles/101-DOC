class Quizbrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        usrval = input(f"Q.{self.question_number}: {current_question.text} (True or False?)")
        self.check_answer(usrval, current_question.answer)

    # this is better than using a loop because I wont get index error at end
    def still_has_questions(self): 
        return self.question_number < len(self.question_list)

    def check_answer(self, usrval, obj):
        if usrval.lower() == obj.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was {obj}")
        print(f"Your current score is: {self.score} / {self.question_number}")

    def game_screen(self):
        print("That's the end of the game")
        

