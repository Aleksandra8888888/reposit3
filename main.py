def read_data_file(file_name):  # обращается к имени файла
    file_lines = []  # создаем пустой список
    file = open(file_name, 'r')  # открываем файл
    for line in file:
        file_lines.append(line)
    return file_lines  # возвращает строки из файла


def split_line(line): #создали функцию, присвоили ей лайн(называем как хотим)
    splited_line = line.split(';') #разбитые строки мы разделяем по точке с запятой
    return splited_line


if __name__ == '__main__':
    stroki_iz_faila = read_data_file('data.csv')
    for stroka in stroki_iz_faila:
        razbitaia_stroka = split_line(stroka)
        print(razbitaia_stroka)
        print(
            f'Меня зовут {razbitaia_stroka[0]},{razbitaia_stroka[1]},мой гендер {razbitaia_stroka[2]},'
            f'год моего рождения {razbitaia_stroka[3]}, можете звонить мне по телефону {razbitaia_stroka[4]}')
