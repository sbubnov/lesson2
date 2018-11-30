answers = {
    'привет': 'Привет!',
    'как дела': 'Отлично, как у тебя?',
    'чем занимаешься': 'Программирую',
    'пока': 'Пока!'
}


def get_answer(question):
    return answers.get(question)


def ask_user(answers):
    try:
        while True:
            user_input = input('Скажите что-нибудь:\n')
            answer = get_answer(user_input)
            print(answer) 

            if user_input == 'пока':
                break
    except(KeyboardInterrupt):
        print('Пока!')
        pass

if __name__ == '__main__':
    ask_user(answers)