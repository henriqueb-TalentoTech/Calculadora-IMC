import math


print("Calculadora de IMC e Composição Corporal - Método das 7 Dobras\n")

# Informações pessoais

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura (Em metro): "))

print("\nInforme as medidas das dobras em milíetros\n")

# Dobras cutâneas

peitoral = float(input("Peitoral: "))
abdominal = float(input("Abdominal: "))
coxa = float(input("abdominal: "))
triceps = float(input("Tríceps: "))
subEscapular = float(input("Sub-escapular: "))
suprIliaco = float(input("Supra-ilíaco: "))
axilar = float(input("Axilar: "))

# Cáluculo IMC

imc = peso / (altura ** 2)
print(f"\nIMC: {imc:.2f}")


# Classificação IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc < 25:
    print("Classificação: Peso normal.")
elif imc < 30:
    print("Classificação: Sobrepeso.")
else:
    print("Classificação: Obesidade.")
    
    