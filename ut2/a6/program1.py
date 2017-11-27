import sys

sentence = sys.argv[1]

def count_words(sentence):
    summary = {}
    list_words = sentence.split(" ")
    for char in list_words:
        if char in summary:
            summary[char] += 1
        else:
            summary[char] = 1
    return summary
for name, number in (count_words(sentence)).items():
    print(name + ":" + str(number))
