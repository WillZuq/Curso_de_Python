a = 'A';
b = 'B';
c = 1.1;
formato_1 = 'a = {} b = {} c = {:.2f}'.format(a, b, c);
formato_2 = 'b = {1} a = {0} a = {0} c {2}'.format(a, b, c); # {index}, semelhante a vetor

print(formato_1);
print(formato_2);
