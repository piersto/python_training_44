from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.name)

    '''Функция для сравнения по смыслу, а не по физическому расположению обЪектов. 
    Принимает в качестве второго параметра объект, с которым мы должны сравнить текущий объект self.
    Теперь наши объекты будут сравниваться при помощи этой функции, то есть будет выполняться
    сравнение по смыслу, а не по физическому расположению объектов.'''
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name is None or other.name is None or self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
