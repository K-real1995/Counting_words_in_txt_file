import string


def strip_punctuations(line):
    for character in string.punctuation:
        line = line.replace(character, "")

    return line


filepath = 'resourse_1.txt'
word_count = {}

with open(filepath, 'r') as file:
    for line in file:
        line = strip_punctuations(line)
        words = line.split()

        for word in words:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

all_words = list(word_count.keys())


def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values


top_words = order_dict_by_freq(word_count)
for tuple_freq in top_words:
    count, word = tuple_freq
    print("{0:15}{1:8d}".format(word, count))
