print("=" * 40)
print ("BEM-VINDO À CALCULADORA DE IMC")
print("=" * 40)

def ler_peso():
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")

    return peso

peso = ler_peso()




def ler_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros: "))
            if altura <= 0:
                print("A altura deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")
    return altura

altura = ler_altura()

def calcular_imc():
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc()


print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
