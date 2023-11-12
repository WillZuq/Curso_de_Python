#Try, except, else e finally
a = 18
b = 0;
# c = a / b;
try:
    c = a / b;
except ZeroDivisionError:
    print('Dividiu por zero');
except NameError:
    print('Variável não definida');
except Exception:
    print('ERRO');
print('Continuar')