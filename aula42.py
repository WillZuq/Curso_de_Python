frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'
#print(frase.count('Python'));
letra_atual = '';
contador = 0;
qtd_maior = 0;
letra_apareceu_mais_vezes = '';
i = 0;
while i < len(frase):
    letra_atual = frase[i];
    if letra_atual == ' ':
        i += 1;
        continue
    contador = frase.count(letra_atual)
    if qtd_maior < contador:
        qtd_maior = contador;
        letra_apareceu_mais_vezes = letra_atual;
    i += 1;
print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}" e apareceu {qtd_maior} vezes')