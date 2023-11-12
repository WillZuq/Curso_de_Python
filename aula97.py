# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte
# O Python conhece a pasta onde o __main__ está e abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ padrão
# O pyhton conhece todos os módulos e pacotes presentes nos caminhos de sys.path
import aula97_m
print('Este módulo se chama', __name__);
print(aula97_m.variavel_modulo);
aula97_m.soma(3, 4);