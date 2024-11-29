class Programmer:

    def code(self):
        print("我可以写代码和bug")

    # def cook(self):
    #     print("我可以写做饭的代码")


class Cook:

    def cook(self):
        print("我可以做饭")


class Person(Programmer, Cook):
    pass


person = Person()
person.code()
person.cook()

