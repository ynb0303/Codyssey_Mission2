question = "파이썬을 만든 사람의 이름은?"
answer = "귀도"

user_answer = input(question + " ")
if user_answer == answer:
    print("정답입니다!")
else:
    print("틀렸습니다. 정답은 " + answer + "입니다.")
