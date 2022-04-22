# Во внешнем файле resourse_1.txt дан текст. Выведите все слова, встреча-
# ющиеся в тексте, по одному на каждую строку, через пробел укажите ко-
# личество повторений. Слова должны быть отсортированы по убыванию
# их количества появления в тексте, а при одинаковой частоте появле-
# ния — в лексикографическом порядке. Вывод должен осуществляться в
# текстовый файл result_1.txt. При необходимости можно продублировать
# вывод в консоль.
import string


# Функция убирает пунктуацию
def strip_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")

    return line


# Кладем относительный путь к файлу в переменную filepath и создаем пустой словарь для добавления слов и их количества
filepath = 'resourse_1.txt'
word_count = {}

# Открываем файл, убираем пунктуацию, добавляем слова в качестве ключа, если слово повторяется, увеличиваем значение на 1,
# приводим все слова в файле к нижнему регистру
with open(filepath, 'r', encoding='utf-8') as file:
    for line in file:
        line = strip_punctuations(line)
        words = line.split()

        for word in words:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1


# Функция сортировки ключей и значений
def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values, key=lambda word: word[1], reverse=True)
    sorted_values = sorted(sorted_values, key=lambda word: word[0], reverse=False)
    sorted_values = sorted_values[::-1]
    return sorted_values


# Записываем обработанные данные в файл.
with open('result_1.txt', 'w', encoding='utf-8') as file2:
    top_words = order_dict_by_freq(word_count)
    for tuple_freq in top_words:
        count, word = tuple_freq
        result = "{} {}\n".format(word, count)
        file2.write(result)
