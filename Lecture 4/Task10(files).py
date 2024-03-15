# # colors = ['red', '8898', 'blue']
# # data = open('file.txt', 'a', encoding='utf-8') # открываем файл с указание режима работы 'a'
# # data.writelines(colors) # разделителей не будет
# # data.close()

# with open('file.txt', 'w') as data: #все что есть в файле будет перезаписано 
#     data.write('line 1\n')
#     data.write('line 2\n')

path = 'file.txt'
data = open('file.txt', 'r')
for line in data: # печатаем содержимое файла
    print(line)
data.close()