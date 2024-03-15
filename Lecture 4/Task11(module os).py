# os.chdir(path)-смена текуще директории
import os
os.chdir('C:/Users')


# os.getcwd() - текущая рабочая директория
print(os.getcwd())

#os.path.basename('C:/Users/main.py') выведет main.py - базовое имя пути
os.path.basename('C:/Users/main.py')

#print(os.path.abspath('main.py')) выведет 'C:/Users/main.py'