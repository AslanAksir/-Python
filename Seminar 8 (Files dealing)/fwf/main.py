# f = open('data.txt', 'r', encoding='utf-8')
# print(f.readline()) #считывает одну строку и при печати создает пустую строку, поскольку в файле в конце знак абзаца (\n)
# print(f.readlines()) # считывает все строки, с добавлением символа (\n) при печати там, где в конце сторки стоит знак абзаца
# # поскольку после последнего слова знака абзаца нет пустая стока в конце не выводится
# f.close()

def clear_and_write():
    with open('data.txt', 'w', encoding='utf-8') as file: #перезапишет содержимое файлы на "Anna\n"
            file.write("Anna\n")
            # print(f.readlines())

def append_row():
    with open('data.txt', 'a', encoding='utf-8') as file: # добавит к содержимому файла "Ivan\n"
        file.write("Ivan\n")

