# Ręczne tworzenie klasy na podstawie jej elementów

# Metody
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

# Tworzenie klasy
import types

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))

if __name__ == '__main__':
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s.cost())
