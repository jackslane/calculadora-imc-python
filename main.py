# Cabeçalho

print("=" * 40)
print ("BEM-VINDO À CALCULADORA DE IMC")
print("=" * 40)

# Entrada de dados

def ler_peso():
    while True:
        try:
            peso = float(input("Digite seu peso em kg: ").replace(",","."))
            if peso <= 0:
                print("O peso deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")

    return peso


def ler_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros: ").replace(",","."))
            if altura < 0.5 or altura > 2.5:
                print("Digite uma altura entre 0,5 e 2,5.")
                continue
            if altura <= 0:
                print("A altura deve ser maior que zero.")
                continue

            break
        except ValueError:
            print("Digite um número válido.")
    return altura

# Cálculo

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Classificação

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Execução do programa

while True:
    peso = ler_peso()
    altura = ler_altura()
    imc = calcular_imc(peso, altura)

    print(f"\nSeu IMC é: {imc:.2f}")

    classificacao = classificar_imc(imc)
    print(f"Classificação: {classificacao}")

    resposta = input("\nDeseja calcular outro IMC?: (s/n) ")

    if resposta.lower() == "n":
     print("\nPrograma encerrado.")
     break
