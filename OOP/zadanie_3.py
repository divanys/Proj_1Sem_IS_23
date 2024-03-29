    # Николай - оригинальный человек.
    # Он решил создать класс Nikola, принимающий при инициализации 2 параметра:
    # имя и возраст. Но на этом он не успокоился.
    # Не важно, какое имя передаст пользователь при создании экземпляра,
    # оно всегда будет содержать "Николая"
    # В частности - если пользователя на самом деле зовут Николаем,
    # то с именем ничего не произойдет, а если его зовут, например, Максим,
    # то оно преобразуется в "я не Максим, а Николай".
    # Более того, никаких других атрибутов и методов у экземпляра
    # не может быть добавлено, даже если кто-то и
    # вздумает так поступить (т.е. если некий пользователь решит
    # прибавить к экземпляру свойство «отчество» или метод «приветствие»,
    # то ничего у такого хитреца не получится)

class Nikola:
    name = str()
    age = int()
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prints(self):
        ls = [self.name, self.age]
    
    def __del__(self):
        ls = [self.name, self.age]
        if self.name == 'Николай':
            self.name = self.name
        else:
            self.name = f'Я не {self.name}, а Николай'

        print(self.name)

if __name__ == '__main__':
    a = Nikola('Максим', 20)
    b = Nikola('Николай', 24)





