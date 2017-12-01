import sys

def count_words(sentence):
    summary = {}
    listw = sentence.split(" ")
    for count in listw:
        if count in summary:
            summary[count] += 1
        else:
            summary[count] = 1
    return summary

sentence = sys.argv[1]
bucle = count_words(sentence).items()

for names, numbers in bucle:
    print(names + ":" + str(numbers))
