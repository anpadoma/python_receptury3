def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)      # --> 14

def test1():
    x = 0
    exec('x += 1')
    print(x)      # --> 0

def test2():
    x = 0
    loc = locals()
    print('Przed:', loc)
    exec('x += 1')
    print('Po:', loc)
    print('x =', x)

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)
 
def test4():
    a = 13
    loc = { 'a' : a }
    glb = { }
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

if __name__ == '__main__':
    print(':::: Uruchomienie test()')
    test()

    print(':::: Uruchomienie test1()')
    test1()

    print(':::: Uruchomienie test2()')
    test2()

    print(':::: Uruchomienie test3()')
    test3()

    print(':::: Uruchomienie test4()')
    test4()

 

 

