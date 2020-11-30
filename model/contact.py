from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, birthday=None, birth_month=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.birthday = birthday
        self.birth_month = birth_month
        self.id = id

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.lastname, self.firstname)

    '''Функция для сравнения по смыслу, а не по физическому расположению обЪектов. 
    Принимает в качестве второго параметра объект, с которым мы должны сравнить текущий объект self.
    Теперь наши объекты будут сравниваться при помощи этой функции, то есть будет выполняться
    сравнение по смыслу, а не по физическому расположению объектов.'''
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.lastname is None or other.lastname
                        is None or self.lastname == other.lastname) and \
                            (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
