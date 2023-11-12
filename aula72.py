# Exercícios
#Crie uma função que multiplica todos os argumentos
#não nomeados recebeidos.
#Retorne o total para uma variável e mostre o valor da variável.
def multiplicacao(*args):
    total = 1;
    for numero in args:
        total *= numero;
    return total
print(multiplicacao(1, 2, 3, 4, 5));


#Crie uma função que fala se um número é par ou ímpar.
#Retorne se o número é par ou ímpar
def par_ou_impar (a):
    if a % 2 == 0:
        print('É par!!!');
    else:
        print('É impar');
par_ou_impar(6);