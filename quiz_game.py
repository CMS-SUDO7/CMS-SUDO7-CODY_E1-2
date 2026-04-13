import json
import os
from quiz import Quiz

STATE_FILE = "state.json"


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    # ----------------------
    # 데이터 처리
    # ----------------------
    def load_data(self):
        if not os.path.exists(STATE_FILE):
            print("📂 파일 없음 → 기본 데이터 로드")
            self.load_default_quizzes()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data["best_score"]

        except Exception:
            print("⚠️ 파일 손상 → 초기화")
            self.load_default_quizzes()

    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(STATE_FILE, "w", encoding="utf-8", errors="ignore") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_default_quizzes(self):
        self.quizzes = [
            Quiz("한국의 수도는?", ["서울", "부산", "대구", "인천"], 1),
            Quiz("일본의 수도는?", ["오사카", "도쿄", "교토", "나고야"], 2),
            Quiz("미국의 수도는?", ["뉴욕", "LA", "워싱턴 D.C.", "시카고"], 3),
            Quiz("프랑스 수도는?", ["파리", "리옹", "니스", "마르세유"], 1),
            Quiz("영국 수도는?", ["맨체스터", "런던", "리버풀", "브리스톨"], 2),
        ]

    # ----------------------
    # 입력 처리
    # ----------------------
    def input_number(self, prompt, min_val, max_val):
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    print("❗ 입력 필요")
                    continue

                num = int(value)

                if num < min_val or num > max_val:
                    print("❗ 범위 오류")
                    continue

                return num

            except ValueError:
                print("❗ 숫자만 입력")
            except (EOFError, KeyboardInterrupt):
                print("\n⚠️ 안전 종료")
                self.save_data()
                exit()

    # ----------------------
    # 기능들
    # ----------------------
    def play_quiz(self):
        if not self.quizzes:
            print("퀴즈 없음")
            return

        score = 0

        for quiz in self.quizzes:
            quiz.display()
            ans = self.input_number("정답: ", 1, 4)

            if quiz.check_answer(ans):
                print("✅ 정답")
                score += 1
            else:
                print("❌ 오답")

        print(f"\n점수: {score}/{len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("🏆 최고 점수 갱신!")

        self.save_data()

    def clean_text(self, text):
     return text.encode("utf-8", "ignore").decode("utf-8")

    def add_quiz(self):
        question = input("문제: ").strip()
        choices = []

        for i in range(4):
            choices.append(input(f"선택지 {i+1}: ").strip())

        answer = self.input_number("정답 번호(1~4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("➕ 추가 완료")

    def delete_quiz(self):
        if not self.quizzes:
            print("삭제할 퀴즈 없음")
            return

        print("\n📋 퀴즈 목록")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

        index = self.input_number("삭제할 번호: ", 1, len(self.quizzes))

        deleted = self.quizzes.pop(index - 1)

        self.save_data()
        print(f"🗑 삭제 완료: {deleted.question}")

    def show_quizzes(self):
        if not self.quizzes:
            print("퀴즈 없음")
            return

        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

    def show_score(self):
        print(f"🏆 최고 점수: {self.best_score}")

    # ----------------------
    # 메뉴
    # ----------------------
    def menu(self):
        while True:
            print("\n==== QUIZ GAME ====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 퀴즈 삭제")
            print("6. 종료")

            choice = self.input_number("선택: ", 1, 6)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.delete_quiz()
            elif choice == 6:
                self.save_data()
                print("종료")
                break