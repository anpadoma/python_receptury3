def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} musi być typu {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop

# Przykład zastosowania
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = Person('Dawid', 39)
    p.name = 'Gucio'
    try:
        p.age = 'Stary'
    except TypeError as e:
        print(e)

