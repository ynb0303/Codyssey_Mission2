class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer
    def check(self, user_answer):
        return user_answer == self.answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question_text, answer):
        new_question = Question(question_text, answer)
        self.questions.append(new_question)

    def start(self):
        for q in self.questions:
            user_answer = input(q.question_text + " ")
            if q.check(user_answer):
                print("정답입니다!")
                self.score += 1
            else:
                print("틀렸습니다. 정답은 " + q.answer + "입니다.")
        print("최종 점수: " + str(self.score) + " / " + str(len(self.questions)))

quiz = Quiz()
quiz. add_question("파이썬을 만든 사람의 이름은?", "귀도")
quiz. add_question("1 + 1은?", "2")
quiz. add_question("대한민국의 수도는?", "서울")    
quiz. start()
