# Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir.

# A  B C     D      Resultado
# 1  2 True  False
# 10 3 False False
# 5  1 True  True

a = 1 > 2 and True or False
b = 10 > 3 and False or False
c = 5 > 1 and True or True

print(a)
print(b)
print(c)