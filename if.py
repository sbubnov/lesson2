print('Введите ваш возраст:')
age=input()

def choose_your_activity():
    your_age = int(age)
    if your_age<=5:
        go_to='в детский сад'
    elif your_age<=16:
        go_to='в школу'
    elif your_age<=21:
        go_to='в ВУЗ'
    elif your_age<=59:
        go_to='работать в поте лица'
    else:
        go_to='думать о вечном'
    return go_to

result=choose_your_activity()
print('Вам нужно '+result)
