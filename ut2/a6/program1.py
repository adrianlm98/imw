import sys

sentence = sys.argv[1]
def count_words(sentence):
    summary = {}
    listw = sentence.split(" ")
    for char in listw:
        if char in summary:
            summary[char] += 1
        else:
            summary[char] = 1
    return summary
for names, numbers in (count_words(sentence)).items():
    print(names + ":" + str(numbers))
