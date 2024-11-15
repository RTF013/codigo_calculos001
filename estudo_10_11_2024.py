
def somando_numeros():
    soma01 = int(input('Digite seu numero para somar: '))
    soma02 = int(input('Digite seu numero para somar: '))
    print('*' * 45)
    somatoria = soma01 + soma02
    return soma01, soma02,  somatoria

def multiplicando_numeros():
    multiplicar01 = int(input('Digite seu numero para multiplicar: '))
    multiplicar02 = int(input('Digite seu numero para multiplicar: '))
    print('*' * 45)
    multiplicar = multiplicar01 * multiplicar02
    return multiplicar01, multiplicar02, multiplicar

def dividir_numeros():
    dividir01 = int(input('Digite seu numero para dividir: '))
    dividir02 = int(input('Digite seu numero para dividir: '))
    print('*' * 45)
    if dividir02 == 0:
        return dividir01, dividir02, 'falsa, não se pode dividir por 0'
    dividir = dividir01 / dividir02
    return dividir01, dividir02, dividir

soma_num1, soma_num2, resultado  = somando_numeros()
multiplica_num01, multiplica_num02, resultado_multiplicar = multiplicando_numeros()
dividir01, dividir02, resultado_dividir = dividir_numeros()

print(f'A soma de {soma_num1} por {soma_num2}  é: {resultado} ')
print(f'A multiplicação de {multiplica_num01} por {multiplica_num02} é: {resultado_multiplicar} ')
print(f'A divisão de  {dividir01} por {dividir02} é: {resultado_dividir} ')

