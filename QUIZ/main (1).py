questions = ("How many countries are in Europe?: ",
             "What is the strongest phone in the world?: ",
             "How many letters are in the Chinese alphabet?: ",
             "What is the hardest language to learn?: ",
             "How many bhp does Koenigsegg Jesko Absolut have?: ")

options = (("A. 42", "B. 46", "C. 44", "D. 39"),
           ("A. NOKIA 3310", "B. SAMSUNG GALAXY NOTE 7", "C. SONIM XP3300 FORCE", "D. IPHONE SE2"),
           ("A. 36", "B. 45", "C. 5,000", "D. 20,000"),
           ("A. HUNGARIAN", "B. MANDARIN", "C. CHINESE", "D. JAPANESE"),
           ("A. 1000", "B. 950", "C. 1320", "D. 1280"))

answers = ("C", "C", "A", "B", "D")
guesses = []
score = 0

for i in range(len(questions)):
    print("WHO WANTS TO BE A BILLIONAIRE")
    print("-------------------------------------")
    print(questions[i])
    for option in options[i]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[i]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[i]} is the correct answer")

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("Answers: ", " ".join(answers))
print("Guesses: ", " ".join(guesses))

percentage_score = score / len(questions) * 100
print(f"Your score is: {percentage_score}%")