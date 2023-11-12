# Generator expression, Iterables e Iteradores em Python
import sys 
iterable = ['Eu', 'Tenho', '__iter__'];
iterator = iter(iterable); #tem __iter__ e __next__;
print(next(iterator));
lista = [n for n in range(100)];
generator = (n for n in range(100));
print(generator);
print(sys.getsizeof(generator));
print(sys.getsizeof(lista));