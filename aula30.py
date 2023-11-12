"""
    CONSTANTE = "Variáveis" que não vão mudar
    Muitas condições no mesmo if (ruim)
        <- Contagem da complexidade (ruim)
"""
velocidade = 61; # velocidade atual do carro
local_carro = 101; # local em que o carro está na estrada

radar_1 = 60; #velocidade máxima do radar 1
local_1 = 100 # local onde o radar 1 está
radar_range = 1 # A distância onde o radar pega

# if velocidade > radar_1:
#     print('Velocidade do carro passou do radar 1');
# if local_carro >= (local_1 - radar_range) and local_carro <= (local_1 + radar_range) and velocidade > radar_1:
#     print('Carro multado em radar');
carro_passou_velocidade = velocidade > radar_1;
carro_passou_radar = local_carro >= (local_1 - radar_range) and local_carro <= (local_1 + radar_range);
if carro_passou_velocidade and carro_passou_radar:
    print('Carro multado no radar 1');




