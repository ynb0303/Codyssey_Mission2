class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 질문
        self.choices = choices      # 보기 리스트 ["①아이언맨", ...]
        self.answer = answer        # 정답 번호 (1~4)

    @classmethod
    def from_dict(cls, data):
        """딕셔너리 → Quiz 객체"""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"]
        )

    def to_dict(self):
        """Quiz 객체 → 딕셔너리 (저장용)"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    def display(self):
        """문제 출력"""
        print(f"\n❓ {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        """정답 확인 (True/False)"""
        return self.answer == user_answer