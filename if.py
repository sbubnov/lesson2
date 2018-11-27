print('Введите ваш возраст:')
age=input()

def choose_your_activity():
    if int(age)<=5:
        go_to='в детский сад'
    elif int(age)<=16:
        go_to='в школу'
    elif int(age)<=21:
        go_to='в ВУЗ'
    elif int(age)<=59:
        go_to='работать в поте лица'
    else:
        go_to='думать о вечном'
    return go_to

result=choose_your_activity()
print('Вам нужно '+result)
