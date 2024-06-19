# Design a quiz program that asks the user a series of questions and then provides a score at the end.

print("Welcome to Be a Star Quiz")
print()

# a list of dictionaries
quiz_questions = [{"question":"How many States do we have in Nigeria?", "answer":"36"},
            {"question":"How many countries are there in Africa?","answer":"54"},
            {"question":"How many vowels do we have in English language?","answer":"5"},
            {"question":"How many consonants do we have in English language?","answer":"21"},
            {"question":"What is the capital of Ghana?", "answer":"Accra"},
            {"question":"Who is the current president of USA?", "answer":"Joe Biden"}]

# i have to give the user a default score of zero
score = 0

for question in quiz_questions:
    print(question["question"])
    answer = input("Enter your answer: ")
    # i want the answer with strings to be case insensitive
    if answer.lower() == question["answer"].lower():
        print("You are correct!")
        score += 1
    else:
        print(f"Sorry, you got it wrong")

print(f"\nYour final score is {score} out of {len(quiz_questions)}")
    