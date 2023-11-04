import random

#Funtion to load questions from a file 
def load_questions(quiz_questions):
    with open(quiz_questions, 'r') as file:
        lines = file.read().split('\n\n')
    questions = []
    for block in lines:
        question_lines = block.split('\n')
        question = question_lines[0]
        options = [line[3:] for line in question_lines if line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D.")]
        correct_answer = next(line for line in question_lines if line.startswith("Correct Answer:"))[:]
        questions.append({'question': question, 'options': options, 'correct_answer': correct_answer})
    return questions

#Funtion to present a qution and get the user's answer
def present_question(question_data):
    for i, option in enumerate(question_data['options'][:4], start=1):
        print(f'{chr(64 + i)}. {option}')
    user_answer = input('Enter the letter of your answer (A, B, C, or D): ')
    return user_answer.upper()

#Funtion to evaluate the user' answer and keep track of the score
def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'Incorrect. The correct answer is option {correct_answer}')
        return False
    

#Function to display final result
def display_results(score, total_questions):
    print(f'your final score is: {score}/{total_questions}')
    if score == total_questions:
        print('Congratulation! .you got all the questions right.')
    elif score >= total_questions / 2:
        print('Good job! you did well.')
    else:
        print('Keep practicing. you can do better!')

#Load questions from the file
quiz_questions = load_questions('quiz_questions.txt')

#Main game loop
while True:
    random.shuffle(quiz_questions)
    score = 0
    total_questions =len(quiz_questions)


    print('Welcome to the Quiz Game!')
    print('You will be asked a series of multiple-choicequestions. choose the correct answer.')

    for question_data in quiz_questions:
        user_answer = present_question(question_data)
        if evaluate_answer(user_answer,question_data['correct_answer']):
            score += 1
    
    display_results(score,total_questions)

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break

print('Thank You for playing the quiz Game!')