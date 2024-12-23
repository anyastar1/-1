#3 задание проверка файла на существование
try:
    def f(x,y):

       with open(x, 'r') as file:
        if y=='full':
            print(file.read())
        if y=='line':
            for line in file:
                print(line)
    y=input('Введите full  для полного чтения или line для построчного')
    f('examlle.txt',y)
except FileNotFoundError:
    print('Такого файла нет')
