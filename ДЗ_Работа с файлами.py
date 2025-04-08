#1. Создайте текстовый файл data.txt и запишите в него несколько строк текста.
with open('data.txt', 'w') as file:
    file.write('First string\n')
    file.write('Second string\n')
    file.write('Third string\n')
# 2.Напишите программу, которая открывает этот файл и выводит его содержимое на экран.
with open('data.txt', 'r') as file:
    print(file.read())
# 3. Дополните файл новыми строками с помощью режима добавления 'a'.
with open('data.txt', 'a') as file:
    file.write('Fourth string')
    file.write('\nFifth string')
# 4.Реализуйте чтение содержимого файла построчно и выведите его на экран.
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
# 5. Скопируйте файл в бинарном режиме, создав его копию с другим именем.
with open('data.txt', 'rb') as file:
    with open('data_copy.txt', 'wb') as copy_file:
        copy_file.write(file.read())

# 6. Проверка "data_copy"
with open('data_copy.txt', 'r') as file:
    print(file.read())