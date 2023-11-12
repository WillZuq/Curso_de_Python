#try, except, else e finally
try:
    print('ABRIU ARQUIVO');
    8/0
except ZeroDivisionError:
    print('DIVIDIU ZERO');
finally:
    print('FECHAR ARQUIVO');