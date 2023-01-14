# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

from string import punctuation   # Библиотека, позволяющая найти все знаки препинания.

punctuationStr = 0

my_file = open("text18-3.txt", "r", encoding="utf-8")   # Открытие исходного текста.
text = my_file.readlines()
print('--*--*--*--*-стихотворение-*--*--*--*--\n')
print("".join(text), '\n')
print("--*--*--*--*--*--*--*--*--*--*--*--*--\n")
my_file.close()

for i in text[0:4]:   # Вычисление количества знаков пунктуации.
    k = list(i)
    for j in k:
        if j in punctuation:
            punctuationStr += 1

print(f"Колличество знаков пунктуации: {punctuationStr}", '\n')
print("--*--*--*--*--*--*--*--*--*--*--*--*--\n")

my_file = open("text18-3.txt", "r", encoding="utf-8")   # Открываем исходный текст и создаём новый файл.
new_file = open("new_file.txt", "w", encoding="utf-8")

# Добавляем текст новый файл с заменой третьей строки на числовой код.
text2 = [str(ord(str(i))) for i in text[2]]
for line in range(len(text)):
    if line == 2:
        new_file.writelines(' '.join(str(j) for j in text2))
    else:
        new_file.write(text[line])

my_file.close()
new_file.close()