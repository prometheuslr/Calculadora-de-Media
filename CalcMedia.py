print('Calculadora de Média\n')
PrimNot=float(input('Digite a primeira nota:\n'))
while PrimNot<0:
    PrimNot=float(input('Digite a primeira nota:\n'))
SegNot=float(input('Digite a segunda nota:\n'))
while SegNot<0:
    SegNot=float(input('Digite a segunda nota:\n'))
print('A média do alunoª é',(PrimNot+SegNot)/2)
