def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0
    for key in questions:
        question_num += 1
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)

    display_score(correct_guesses, len(questions))

    play_again()

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0

def display_score(correct_guesses, total_questions):
    print("----------")
    print("Quiz Results")
    print("----------")
    percentage = (correct_guesses / total_questions) * 100
    print(f"You got {correct_guesses} out of {total_questions} questions correct.")
    print(f"Your score: {percentage}%")

def display_project():
    print("Welcome to the Python Quiz!")
    print("Test your knowledge about Python with these questions.")
    print("Choose the correct option (A, B, C, or D) for each question.")

def play_again():
    while True:
        choice = input("Do you want to play again? (Y/N): ")
        choice = choice.upper()
        if choice == "Y":
            new_game()
        elif choice == "N":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter Y or N.")

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is attributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

display_project()
new_game()
