"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""
import decimal;
num_1 = 0.1;
num_2 = 0.7;
num_3 = num_1 + num_2;
numero_1 = decimal.Decimal('0.1');
numero_2 = decimal.Decimal('0.7');
numero_3 = numero_1 + numero_2;
print(num_3);
print(f'{num_3:.2f}');
print(round(num_3, 2));
print(numero_3);


