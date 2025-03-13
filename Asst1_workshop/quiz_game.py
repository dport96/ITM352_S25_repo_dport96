QAs = [
    {
        "question": "What is the airspeed of an unladen swallow in miles/hr?",
        "options": ["12", "8", "11", "15"],
        "answer_index": 0
    },
    {
        "question": "What is the capital of Texas?",
        "options": ["Austin", "San Antonio", "Dallas", "Waco"],
        "answer_index": 0
    },
    {
        "question": "The Last Supper was painted by which artist?",
        "options": ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"],
        "answer_index": 0
    },
    {
        "question": "Which classic novel opens with the line 'Call Me Ishmael'?",
        "options": ["Moby Dick", "Wuthering Heights", "The Old Man and the Sea", "The Scarlet Letter"],
        "answer_index": 0
    },
    {
        "question": "Frank Lloyd Wright designed a house that included a waterfall. What is the name of this house?",
        "options": ["Fallingwater", "Watering Heights", "Mossyledge", "Taliesin"],
        "answer_index": 0
    }
]


def ask_question(QAs_dict):
    print(QAs_dict['question'])
    # print the options
    i = 0
    for option in QAs_dict['options']:
        print(f'{chr(97 + i)}) {option}')
        i += 1
     
    answer = input("Your answer: ")
    # check if answer is valid
    
    # convert answer label to option index
    answer_index = 97 - ord(answer.lower())
    if answer_index == QAs_dict['answer_index']:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is: {QAs_dict['options'][QAs_dict['answer_index']]}\n")
        
ask_question(QAs[0])
ask_question(QAs[1])