import sys

sentence = sys.argv[1]

def count_words(sentence):
    summary = {}
    listw = sentence.split(" ")
    for count in listw:
        if count in summary:
            summary[count] += 1
        else:
            summary[count] = 1
    return summary
for names, numbers in (count_words(sentence)).items():
    print(names + ":" + str(numbers))
