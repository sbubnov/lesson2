sum=0


def get_sum(num_one, num_two):
    try:
        sum=int(num_one)+int(num_two)
        print(sum)
    except(ValueError):
        print('Вы ввели неправильное значение')
    

get_sum(3.4,'test')
