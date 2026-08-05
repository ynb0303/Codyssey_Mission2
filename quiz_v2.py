questions = [
    {"question": "파이썬을 만든 사람의 이름은?", "answer": "귀도"},
    {"question": "1 + 1은?", "answer": "2"},
    {"question": "대한민국의 수도는?", "answer": "서울"}
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer == q["answer"]:
        print("정답입니다!")
        score = score +1
    else:
        print("틀렸습니다. 정답은 " + q["answer"] + "입니다.")

print("최종 점수: " + str(score) + " / " + str(len(questions)))
