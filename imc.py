massa = float(input('Digite sua massa em g: '))
massa = massa/1000
altura = float(input('Digite a sua altura em cm: '))
altura = altura/100
imc = massa/altura**2

print(f'O seu índice de massa corporal é: {imc} kg/m²')
