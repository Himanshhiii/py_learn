# Python Quiz Game

questions = (
    "What is the capital of France?",
    "Who won the Nobel Prize in Literature in 2020?",
    "Who invented the telephone?",
    "What is the world's largest island?"
)

options = (
    ("A. London", "B. Paris", "C. Washington DC", "D. Delhi"),
    ("A. Kazua Ishiguro", "B. Bob Dylan", "C. Gabriel Garcia Marquez", "D. Louise Gluck"),
    ("A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. Isaac Newton"),
    ("A. Australia", "B. Greenland", "C. New Guinea", "D. Madagascar")
)


answers =("B", "D", "A", "B")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 4
        print("CORRECT!!")
    else:
        score -=1
        print("INCORRECT. The correct answer is: ", options[question_num][answers.index(answers[question_num])])

    question_num +=1

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score= int((score/len(questions) * 100)/4)

print(f"Your score is {score}%")
