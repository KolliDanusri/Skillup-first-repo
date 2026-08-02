import random
import time
import getpass

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "student": {"password": "student123", "role": "student"}
}


questions = [
    {
        "question": "1.Which data type is used to store multiple values in a single variable?",
        "options": ["A. int", "B. string", "C. list", "D. float"],
        "answer": "C"
    },
    {
        "question": "2.Which of the following is used to define a function in python?",
        "options": ["A. func","B. define","C. def","D. function"],
        "answer": "C"
    },
    {
        "question": "3.Which keyword is used to stop a function and return a value?",
        "options": ["A. stop", "B. return", "C. break", "D. exit"],
        "answer": "B"
    },
    {
        "question": "4.Which operator is used for exponentiation?",
        "options": ["A. ^", "B. *", "C. **", "D. //"],
        "answer": "C"
    },
    {
        "question": "5.print(type([])) gives?",
        "options": ["A. <class 'list'>","B. <class 'tuple'>","C. <class 'dict'>","D. <class 'set'>"],
        "answer": "A"
    }
]


TOTAL_QUESTIONS = 5      
TIME_LIMIT = 30          


def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!\n")
        return users[username]["role"]
    else:
        print("Invalid login!\n")
        return None

def take_exam():
    print("\nExam Started!")
    print("You have", TIME_LIMIT, "seconds to complete the exam.")
    print("Total Questions:", TOTAL_QUESTIONS)

    random.shuffle(questions)
    selected = questions[:TOTAL_QUESTIONS]

    start_time = time.time()
    score = 0

    for q in selected:

        # Check if time is over
        if time.time() - start_time > TIME_LIMIT:
            print("\n Time is Over!")
            break

        print("\n", q["question"])
        for opt in q["options"]:
            print(opt)

        remaining = int(TIME_LIMIT - (time.time() - start_time))
        print("Remaining Time:", remaining, "seconds")

        answer = input("Your Answer: ").upper()

        if answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    print("\nRESULT")
    print("Score:", score, "/", TOTAL_QUESTIONS)
    percentage = (score / TOTAL_QUESTIONS) * 100
    print("Percentage:", percentage, "%")


def main():
    while True:
        print("\n ONLINE EXAM SYSTEM ")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            role = login()

            if role == "student":
                take_exam()
            else:
                print("Only student can take exam in this version.")

        else:
            break

main()