from Questions import Question

question_prompts = [
    "Who Am I? \n(a) Larry\n(b) Jon \n(c) Pineapple\n\n",
    "What is my username? \n(a) Pinesol\n(b) KFChinese\n(c) Kek\n\n",
    "What food do I love? \n(a) Sushi\n(b) Sardines\n(c) Durian\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score)+"/" + (str(len(questions)) + " correct!"))


run_test(questions)
