d=input("Введите текст:")
with open('user_input.txt','a') as file:
    file.write(d+'\n')

