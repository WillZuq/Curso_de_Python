# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def erro_divide_por_zero(d):
    if d == 0:
         if d == 0:
            raise ZeroDivisionError('Voce está tentando dividir por zero');
    return True

def divide(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(f'{d} deve ser int ou floar');
    erro_divide_por_zero(d);
    return n /d
print(divide(8, 0));