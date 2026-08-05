import json

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

    def load_questions(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            self.add_question(item["question_text"], item["answer"])

    def start(self):
        for q in self.questions:
            user_answer = input(q.question_text + " ")
            if q.check(user_answer):
                print("정답입니다!")
                self.score = self.score + 1
            else:
                print("틀렸습니다. 정답은 " + q.answer + "입니다.")
        print("최종 점수: " + str(self.score) + " / " + str(len(self.questions)))

    def save_score(self, filename, player_name):
        record = {"name": player_name, "score": self.score, "total": len(self.questions)}

        try:
            with open(filename, "r", encoding="utf-8") as f:
                records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            records = []

        records.append(record)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

quiz = Quiz()
quiz.load_questions("questions.json")
quiz.start()

player_name = input("이름을 입력하세요: ")
quiz.save_score("scores.json", player_name)