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
```
1. 프로그램 시작 화면
<img width="616" height="215" alt="image" src="https://github.com/user-attachments/assets/1a9d95ca-0530-41fd-8296-8f5674e857e0" />

2. 퀴즈 진행 화면
<img width="1583" height="934" alt="스크린샷 2026-04-13 213602" src="https://github.com/user-attachments/assets/e64b97d5-950f-4d8a-94ae-55c34cae1ddf" />

3. 결과 + 최고 점수 갱신
<img width="429" height="114" alt="스크린샷 2026-04-13 213658" src="https://github.com/user-attachments/assets/e939a80a-33cf-4d52-8f9c-ba70aea9cb13" />

4. 퀴즈 추가 화면
<img width="690" height="239" alt="스크린샷 2026-04-13 213828" src="https://github.com/user-attachments/assets/1653770c-7ca5-44f4-8b82-e9d5741e4811" />

5. 퀴즈 목록 확인
<img width="448" height="213" alt="스크린샷 2026-04-13 213847" src="https://github.com/user-attachments/assets/71492cb6-8fe7-4e59-9aba-c8314f242174" />

6. 퀴즈 삭제
<img width="458" height="553" alt="image" src="https://github.com/user-attachments/assets/a883bb62-9678-4b2a-a8ed-e3484921b159" />

7. 점수 확인
<img width="408" height="103" alt="image" src="https://github.com/user-attachments/assets/8215a94a-9116-46da-a290-67804f0dafb5" />

8.잘못된 입력 처리 (중요 ⭐)

<img width="733" height="391" alt="image" src="https://github.com/user-attachments/assets/1673fde5-97f2-455c-ac5f-5d1258b6abbd" />


9.안전 종료 (Ctrl + C)

<img width="491" height="69" alt="image" src="https://github.com/user-attachments/assets/e2109445-0fd4-4c34-a3aa-2c8e3612927e" />
