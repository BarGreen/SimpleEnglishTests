import voc_tests


word_list = []

print("==========================================================")
print("==========================================================")

print("Добро пожаловать в консольную версию EnglishTests!\n")
print("Введите в консоль цифру, соответвующую номеру теста:\n\n" + 
        "1. Обычный тест eng-ru(проверка по всем словам словаря)\n" +
        "2. Тест по категории eng-ru(проверка по конкретной категории слов)\n" +
        "3. Обычный тест ru-eng\n" +
        "4. Тест по категории ru-eng\n")

i = int(input())
if i == 1:
    voc_tests.default_test(word_list, 'ENG')
    print()
elif i == 2:
    print("Введите название группы: ")
    group_name = str(input())
    print()
    voc_tests.group_test(word_list, group_name, 'ENG')
    print()
elif i == 3:
    voc_tests.default_test(word_list, 'RU')
    print()
elif i == 4:
    print("Введите название группы: ")
    group_name = str(input())
    print()
    voc_tests.group_test(word_list, group_name, 'RU')
    print()
