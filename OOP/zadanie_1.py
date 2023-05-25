# 1. Есть класс Person, конструктор которого принимает 
# три параметра (не учитывая self) - 
# имя, фамилию и квалификацию специалиста.
# Квалификация имеет значение заданное по умолчанию, равное еденице.
# 2. У класса Person есть метод, который возвращает строку, # включающую в себя всю информацию о сотруднике.
# 3. Класс Person содержит деструктор, который выводит на экран
# фразу "До свидания, мистер
# (вместо троеточия должны выводиться имя и фамилия объекта).
# 4. В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.

class Person:
    name = str()
    surname = str()
    qualify = int()
    sex = str()
    def __init__(self, name, surname, qualify = 1, sex='male'):
        self.name = name
        self.surname = surname
        self.qualify = qualify
        self.sex = sex

    def prints(self):
        ls = [self.name, self.surname, str(self.qualify)]
        return str(' '.join(ls))

    def __del__(self):
        ls = [self.name, self.surname]
        if self.sex == 'male':
            text = "Mr. "
        else:
            text = "Mrs. "

        print('Goodbye, ' + text + str(' '.join(ls)))

if __name__ == '__main__':
    a = Person("Guram", "Spor", 0)
    b = Person("Dasha", "Suhacheva", 80, "female")
    c = Person("Alisa", "Ivanova", 12, "female")
    d = Person("Natacha", "Gubareve", 55, "female")
    e = Person("Aram", "Velam", 2)

    print(a.prints())
    print(b.prints())
    print(c.prints())
    print(d.prints())
    print(e.prints())
    del(e)
    input('Всё ок')