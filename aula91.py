# Introdução às Generator functions em Python
# Generator = (n for n in range(100));

# def generator(n = 0):
#     yield 1 #Pausar
#     print('Continuando....')
#     yield 2
#     print('Mais uma ...');
#     yield 3
#     print('Vou terminar');
#     return 'ACABOU'

# gen = generator(n = 0);
# print(next(gen));
# print(next(gen));
# print(next(gen));
# print(next(gen));
def generator(n = 0, maximum = 10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return

gen = generator();
for n in gen:
    print(n);