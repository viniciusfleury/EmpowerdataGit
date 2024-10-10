print('--------Calculadora------------')
n1 = float(input("Digite um número:"))
op = input("Coloque o operador:")
while True:
    if op not in ['+', '-', '*', '/']:
        print("Operador deve ser +, -, * ou /")
        op = input("Operador invalido digite um novo:")
    else:
        break
n2 = float(input("Digite o segundo número:"))

print("O resultado é:")
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)