import random

# Function to load questions from a file
def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split the line into question, options, and correct answer
                parts = line.strip().split('|')
                question = parts[0]
                options = parts[1:5]
                correct_answer = parts[5]
                questions.append((question, options, correct_answer))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return questions

# Function to run the quiz
def run_quiz(language, questions):
    score = 0
    # Shuffle the questions and pick 10
    random.shuffle(questions)
    selected_questions = questions[:5]

    for i, (question, options, correct_answer) in enumerate(selected_questions):
        print(f"\nQ{i+1}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        answer = input("Your answer (number or option): ").strip().lower()

        # Check if the answer is correct (either by number or by option)
        if answer == correct_answer or answer == options[int(correct_answer) - 1].lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {options[int(correct_answer) - 1]}")

    print(f"\nYou scored {score} out of 10.")
    return score

# Function to save the user's score
def save_score(username, score):
    with open("scores.txt", "a") as file:
        file.write(f"{username}: {score}/10\n")

# Function to check password validity
def pass_checker(password):
    if len(password) < 8 or len(password) > 12:
        print("Password must be between 8 and 12 characters long.")
        return False
    
    special_characters = ["#", "$", "@"]
    if not any(char in special_characters for char in password):
        print("Password must contain at least one special character: #, $, @")
        return False
    
    if not any(char.isdigit() for char in password):
        print("Password should have at least one digit!")
        return False
    
    if not any(char.isupper() for char in password):
        print("Password should have at least one uppercase letter!")
        return False
    
    print("Password is valid.")
    return True

# Main application loop
def main():
    print("Welcome to the Quiz Game!")
    username = input("Enter your username: ")  # Username is not stored

    # Password prompt and validation
    while True:
        password = input("Enter your password: ")
        if pass_checker(password):
            break  # Exit the loop if the password is valid
        else:
            print("Please try again.")

    while True:
        print("\nChoose a language for the quiz:")
        print("1. Python")
        print("2. Java")
        print("3. C++")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("\nYou have selected Python!")
            questions = load_questions("python_questions.txt")
        elif choice == '2':
            print("\nYou have selected Java!")
            questions = load_questions("java_questions.txt")
        elif choice == '3':
            print("\nYou have selected C++!")
            questions = load_questions("cpp_questions.txt")
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        # Run the quiz and get the score
        score = run_quiz(choice, questions)

        # Save the score in a file
        save_score(username, score)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

