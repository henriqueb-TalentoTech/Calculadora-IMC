import math


print("Calculadora de IMC e Composição Corporal - Método das 7 Dobras\n")

# Informações pessoais

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura (Em metro): "))
certo = 0
while certo != 1:
    sexo = int(input("Masculino [1]\t Feminino [2] "))
    if sexo == 1:
        sexo = "M"
        certo = 1
    elif sexo == 2:
        sexo = "F"
        certo = 1
    else: certo = 0

# IMC
imc = peso / (altura ** 2)

classificacao = None
if imc < 18.5:
    classificacao = "Classificação: Abaixo do peso."
elif imc < 25:
    classificacao = "Classificação: Peso normal."
elif imc < 30:
    classificacao = "Classificação: Sobrepeso."
else:
    classificacao = "Classificação: Obesidade."
    
    
form_imc = f"\nIMC: {imc:.2f}"

print("\nInforme as medidas das dobras\n")

# Dobras cutâneas

triceps = float(input("Tríceps (mm): "))
subEscapular = float(input("Sub-escapular(mm): "))

soma_dobras = triceps + subEscapular
    

if sexo == "M":
    if soma_dobras <= 35:
        percentual_gordura = 1.21 * soma_dobras - 0.008 * (soma_dobras ** 2) + 1.7
    else: 
        percentual_gordura = 0.783 * soma_dobras + 1.6
        
             
# Formatters

form_dobras = f"Soma das dobras: {soma_dobras:.1f} mm\n" 

print(form_imc)
print (classificacao)
print(form_dobras)