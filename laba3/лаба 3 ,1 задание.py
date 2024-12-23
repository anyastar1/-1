#вывод текста всего файла 
def f(x,y):
  if y=='full':
    with open(x, 'r') as file:
      print(file.read())
# построчный вывод содержимого
if y=='line':
    with open(x, 'r') as file:
      for line in file:
          print(line)
y=input('Введите full  для полного чтения или line для построчного')
f('example.txt',y)
