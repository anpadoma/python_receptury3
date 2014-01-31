# Inna wersja krotek nazwanych

import operator
import types
import sys

def named_tuple(classname, fieldnames):
	# Zapełnianie słownika akcesorami z właściwości
    cls_dict = { name: property(operator.itemgetter(n))
                 for n, name in enumerate(fieldnames) }

    # Tworzenie funkcji __new__ i dodawanie jej do słownika klasy
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Oczekiwano {} argumentów'.format(len(fieldnames)))
        return tuple.__new__(cls, (args))

    cls_dict['__new__'] = __new__

    # Tworzenie klasy
    cls = types.new_class(classname, (tuple,), {}, 
                           lambda ns: ns.update(cls_dict))
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls

if __name__ == '__main__':
    Point = named_tuple('Point', ['x', 'y'])
    print(Point)
    p = Point(4, 5)
    print(len(p))
    print(p.x, p[0])
    print(p.y, p[1])
    try:
        p.x = 2
    except AttributeError as e:
        print(e)
    print('%s %s' % p)
