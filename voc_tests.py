import csv
import random

voc_dir = 'voc.csv'

# with open(voc_dir, mode='r', encoding='utf8') as csv_file:   
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(row)

def correct_answers(x, lang):

    true_ans = 0
    if lang == 'ENG':
        for i in random.sample(x, len(x)):
                print(i[0])
                ans = str(input())
                if ans == i[1]:
                    true_ans += 1
    elif lang == 'RU':
        for i in random.sample(x, len(x)):
                print(i[1])
                ans = str(input())
                if ans == i[0]:
                    true_ans += 1

    print('\n' + str(true_ans) + " correct answers out of " + str(len(x)))


def default_test(x, lang):

    with open(voc_dir, mode='r', encoding='utf8') as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter = ";")
        for row in csv_reader:
            x.append([row[0], row[1], row[2]])
        correct_answers(x, lang)


def group_test(x, group_name, lang):

    with open(voc_dir, mode='r', encoding='utf8') as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter = ";")
        for row in csv_reader:
            if row[2] == group_name:
                x.append([row[0], row[1], row[2]])
        correct_answers(x, lang)
