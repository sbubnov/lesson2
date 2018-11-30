def ask_user():
    while True:
        user_say=input('Как дела?\n')
        if user_say=='Хорошо!':
            break
    while True:
        user_say=input('Что делаешь?\n')
        if user_say=='Программирую':
            break

ask_user()