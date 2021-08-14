""" A quiz program. """

art_quiz_bank = [
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "vincent van gogh",
    },
    {
        "question": "What precious stone is used to make the artist\'s pigment ultramarine?",
        "answer": "lapiz lazuli",
    },
    {
        "question": "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?",
        "answer": "chicago",
    },
    
]

space_quiz_bank = [
    {
        "question": "Which planet is closest to the sun?",
        "answer": "mercury",
    },
    {
        "question": "Which planet spins in the opposite direction to all the others in the solar system?",
        "answer": "venus",
    },
    {
        "question": "How many moons does Mars have?",
        "answer": "2",
    },
    
]


def start_quiz(topic, quiz_question_bank):
    """Starts Quiz"""
    total_score = 0
    number_of_quiz_questions = len(quiz_question_bank)
    for question in quiz_question_bank:
        print(question['question'])
        answer = input('Enter your answer: ')
        if answer.lower() == question['answer']:
            print('Correct!')
            total_score += 1
        else:
            print(f'Sorry, the answer is {question["answer"]}.')
            
    print('End of quiz!')
    print(f'Your total score on {topic} questions is {total_score} out of {number_of_quiz_questions}.')
    if total_score == number_of_quiz_questions:
        print('You got all the answers correct!')
    

    

topic = input('Would you like art, or space questions?')

if topic.lower() == "art":
    start_quiz(topic, art_quiz_bank)

elif topic.lower() == 'space':
    start_quiz(topic, space_quiz_bank)
        
else:
    print('That is not a valid topic. Restart the program to try again.')


