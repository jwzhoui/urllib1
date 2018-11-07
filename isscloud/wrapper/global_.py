class Animal(object):
    def __init__(self, name, age):
        # self._name = name
        self._age = age
        self._color = 'Black'
        self.ooo = 22
        self._local = 's'
        self.wlocal2 = 's2'
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, basestring):
            self._name = value
        else:
            self._name = 'No name'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0 and value < 100:
            self._age = value
        else:
            self._age = 0
            # print 'invalid age value.'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value;

    @property
    def local(self):
        return self.wlocal

    #
    # @local.setter
    # def local(self,local):
    #     self.wlocal = local
a = Animal('black dog', 3)
a.name = 'white dog'
a.wlocal = 2
a.wlocal2 = '4'
# print a.__dict__
print a.wlocal
print a.wlocal2
