# создать 5 классов
# в 2 из них есть конструктор (__init__)
# в одном  атрибут name в другом age
# в 2 есть по 1 методу и в последнем классе
# наследовать все классы
# и сделать так чтобы у последнего класса были все методы и атрибуты (name,age) и методы которые вы придумаете
# создать txt файл и написать туда все команды гита которые мы прошли
#
# создать новую ветку с вашим именем и запушить туда!!!
# отправить гит с вашей новой веткой


class s_name:
    def __init__(self, name):
        self.name = name
    def n(self):
        print(f"My name is {self.name}")

class s_age:
    def __init__(self, age):
            self.age = age
    def n(self):
        print(f'I am {self.age} years old')

class s_hobby:
    def n(self):
        print(f'My hobby is coding')

class s_citiz:
    def n(self):
        print(f'I am from Kyrgyzstan')

class data(s_citiz, s_hobby, s_age, s_name):
    def __init__(self, age, name):
        s_age.__init__(self, age)
        s_name.__init__(self, name)

    def n(self):
        s_name.n(self)
        s_age.n(self)
        s_citiz.n(self)
        s_hobby.n(self)

        print(f'Nice to meet you!')

student = data(33, 'Nazira')

student.n()

# print(data.mro())

with open('git.txt', 'w') as f:
    f.write(f'git init\n'
            f'git remote add origin link\n'
            f'create .gitignore\n'
            f'.idea\n'
            f'.gitignore\n'
            f'__pycache__/\n'
            f'venv\n'
            f'git add . or name to file\n'
            f'git commit -m "text"\n'
            f'git push origin name to branch\n'
            f'git remote remove origin\n'
            f'git rm --cached name to file\n'
            f'git rm --cached -r name to dir\n'
            f'git branch\n'
            f'git branch name to branch\n'
            f'git checkout name branch\n'
            f'git checkout -b name to branch\n'
            f'git merge name to branch')