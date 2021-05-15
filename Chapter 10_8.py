def vyvod(filename):
    """Вывод содержимого файла"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, файл {filename} отсутствует!")
        pass
    else:
        print(contents)


# vyvod('cats.txt')
# print ("---------------")
# vyvod('dogs.txt')

def word_count(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        return contents.lower().count(word)


print(f"Количество слов the в книге - {word_count('3.txt', 'the ')}")
