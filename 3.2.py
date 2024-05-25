import json
import csv

# Function to load questions from a JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = json.load(file)
    return questions

# Function to ask questions and get user responses
def conduct_quiz(questions):
    score = 0
    for idx, q in enumerate(questions):
        print(f"Q{idx + 1}: {q['question']}")
        answer = input("Your answer: ")
        if answer.strip().lower() == q['answer'].strip().lower():
            score += 1
    return score

# Function to save user results to a CSV file
def save_results(filename, username, score, total_questions):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, score, total_questions])

def main():
    # Load questions
    questions = load_questions('questions.json')

    # Get user's name
    username = input("Enter your name: ")

    # Conduct the quiz
    score = conduct_quiz(questions)

    # Display the results
    total_questions = len(questions)
    print(f"{username}, you scored {score} out of {total_questions}.")

    # Save the results
    save_results('results.csv', username, score, total_questions)

if _name_ == "_main_":
    main()
