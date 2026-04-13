# 🎮 Quiz Game

## 📌 프로젝트 개요
콘솔 기반 퀴즈 게임으로, 사용자가 문제를 풀고 직접 퀴즈를 추가할 수 있으며  
점수와 데이터는 파일로 저장되어 유지된다.

## 📌 퀴즈 주제 및 선정 이유
주제: 나라별 수도 맞추기

이유:
- 누구나 기본적으로 알고 있는 상식
- 난이도 조절이 쉬움
- 확장성이 좋음 (국가 추가 가능)

## 📌 실행 방법
```bash
python main.py

📌 기능 목록
퀴즈 풀기
퀴즈 추가
퀴즈 목록 확인
최고 점수 확인
데이터 저장 (state.json)

📌 파일 구조
quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
└── README.md

📌 데이터 파일 설명
경로: 프로젝트 루트의 state.json
역할: 퀴즈 + 최고 점수 저장

{
  "quizzes": [
    {
      "question": "문제",
      "choices": ["1", "2", "3", "4"],
      "answer": 1
    }
  ],
  "best_score": 3
}

---

# ✅ 4. Git 커밋 전략 (이거 그대로 하면 10개 채움)

```bash
git init

git add .
git commit -m "Init: 프로젝트 초기 설정"

git commit -am "Feat: 메뉴 기능 구현"
git commit -am "Feat: Quiz 클래스 구현"
git commit -am "Feat: 기본 퀴즈 데이터 추가"

git checkout -b feature/play
git commit -am "Feat: 퀴즈 풀기 기능 구현"
git checkout main
git merge feature/play

git commit -am "Feat: 퀴즈 추가 기능 구현"
git commit -am "Feat: 퀴즈 목록 기능 구현"
git commit -am "Feat: 점수 시스템 구현"
git commit -am "Feat: JSON 저장/불러오기 구현"

git commit -am "Docs: README 작성"

git clone <repo_url>

# 수정 후
git commit -am "Docs: README 한 줄 추가"
git push

# 기존 폴더에서
git pull

1. 프로그램 시작 화면
<img width="616" height="215" alt="image" src="https://github.com/user-attachments/assets/1a9d95ca-0530-41fd-8296-8f5674e857e0" />
