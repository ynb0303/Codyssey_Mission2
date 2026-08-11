import json
import os
from quiz import Quiz

STATE_FILE = "state.json"

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    # ── 저장 / 불러오기 ──────────────────────
    def load_state(self):
        """state.json 불러오기"""
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
        else:
            self.init_default_quizzes()

    def save_state(self):
        """state.json 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("💾 저장 완료!")

    def init_default_quizzes(self):
        """기본 퀴즈 7개 초기화"""
        default_data = [
            {
                "question": "아이언맨의 본명은?",
                "choices": ["스티브 로저스", "토니 스타크", "브루스 배너", "클린트 바튼"],
                "answer": 2
            },
            {
                "question": "어벤져스 엔드게임에서 타노스를 처치한 인물은?",
                "choices": ["아이언맨", "토르", "캡틴 아메리카", "헐크"],
                "answer": 1
            },
            {
                "question": "블랙 위도우의 본명은?",
                "choices": ["나타샤 로마노프", "완다 막시모프", "페퍼 포츠", "마리아 힐"],
                "answer": 1
            },
            {
                "question": "토르의 망치 이름은?",
                "choices": ["건브레이커", "묠니르", "스톰브링어", "엑스칼리버"],
                "answer": 2
            },
            {
                "question": "가디언즈 오브 갤럭시에서 스타로드의 본명은?",
                "choices": ["피터 퀼", "가모라", "드랙스", "로켓"],
                "answer": 1
            },
            {
                "question": "인피니티 스톤은 총 몇 개인가?",
                "choices": ["4개", "5개", "6개", "7개"],
                "answer": 3
            },
            {
                "question": "스파이더맨의 본명은?",
                "choices": ["마일스 모랄레스", "피터 파커", "미겔 오하라", "벤 라일리"],
                "answer": 2
            }
        ]
        self.quizzes = [Quiz.from_dict(q) for q in default_data]
        self.save_state()

    # ── 게임 기능 ──────────────────────────
    def play_quiz(self):
        """퀴즈 풀기"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n🎮 퀴즈 시작! 총 {total}문제")
        print("-" * 30)

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n[{i}/{total}]", end="")
            quiz.display()

            while True:
                try:
                    answer = int(input("\n정답 번호 입력 (1~4): "))
                    if 1 <= answer <= 4:
                        break
                    print("⚠️  1~4 사이 숫자를 입력하세요.")
                except ValueError:
                    print("⚠️  숫자를 입력하세요.")

            if quiz.check_answer(answer):
                print("✅ 정답!")
                score += 1
            else:
                print(f"❌ 오답! 정답은 {quiz.answer}번 입니다.")

        # 결과 출력
        print("\n" + "=" * 30)
        print(f"🏆 최종 점수: {score}/{total}")

        if score > self.best_score:
            self.best_score = score
            print(f"🎉 최고 기록 갱신! {self.best_score}점")
            self.save_state()

    def add_quiz(self):
        """퀴즈 추가"""
        print("\n➕ 새 퀴즈 추가")
        question = input("질문을 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"{i}번 보기: ").strip()
            choices.append(choice)

        while True:
            try:
                answer = int(input("정답 번호 (1~4): "))
                if 1 <= answer <= 4:
                    break
                print("⚠️  1~4 사이 숫자를 입력하세요.")
            except ValueError:
                print("⚠️  숫자를 입력하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        """퀴즈 목록 보기"""
        if not self.quizzes:
            print("❌ 퀴즈가 없습니다.")
            return

        print(f"\n📋 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 30)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    def show_best_score(self):
        """최고 점수 보기"""
        print(f"\n🏆 최고 점수: {self.best_score}/{len(self.quizzes)}")

    # ── 메인 메뉴 ──────────────────────────
    def run(self):
        """게임 실행"""
        print("🦸 마블 퀴즈 게임에 오신 것을 환영합니다!")

        while True:
            print("\n" + "=" * 30)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 최고 점수")
            print("5. 종료")
            print("=" * 30)

            choice = input("메뉴 선택: ").strip()

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_best_score()
            elif choice == "5":
                print("👋 게임을 종료합니다!")
                break
            else:
                print("⚠️  1~5 사이 숫자를 입력하세요.")


if __name__ == "__main__":
    game = QuizGame()
    game.run()