"""
Iterando strings com while
"""
nome = 'Luiz Otávio'; #iteráveis
tamanho_nome = len(nome);
contador = 0;
nova_string = '';
while contador < tamanho_nome:
    nova_string += '*'+nome[contador];
    contador += 1;
print(nova_string);