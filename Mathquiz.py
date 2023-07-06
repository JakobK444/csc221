import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operator} {num2}? "
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
    return question, eval(f"{num1}{operator}{num2}")

def take_math_test():
    print("Have fun on the math test, Try your best!")
    score = 0
    total_questions = 5
    for _ in range(total_questions):
        question, answer = generate_question()
        user_answer = input(question)
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Wrong, please type number.")
    
            continue
        if user_answer == answer:
            score += 1
    print(f"\nYour score: {score}/{total_questions}")
    if score >= 4:
        print("Good job!")
    if score <= 3:
        print("Please Try Again")

take_math_test()