# Importar a biblioteca TIME para usar a funçao SLEEP
from time import sleep 
nome = str(input("Digite o seu nome: "))
sleep(0.5)
idade = int(input(f"Olá, {nome}. Informe a sua idade: "))
sleep(0.5)
peso = float(input("Agora informe o seu peso (KG): "))
sleep(0.5)
altura_float = input("Por ultimo, infome a sua altura. (Em metros. Ex: 1.75 ou 170): ")

# Convertendo a altura em float e em metros
try:
    altura = float(altura_float)
    
    if ( altura >= 100):
        altura = altura/100
        
    print(f"Sua altura registrada foi de {altura:.3} m")

# Caso o usuario informe um numero invalido 
except ValueError:
    print("Entrade invalida! Digite um numero valido: ")

# A conta para saber o IMC
imc = peso/(altura * altura)

# Sleep para o atraso programado do codigo
sleep(1)

# Condiçao do IMC 
if ( imc < 18.5):
    print(f"Seu IMC é {imc:.3}. Voce esta ABAIXO DO PESO.")
elif (18.5 <= imc < 25):
    print(f"Seu IMC é {imc:.3}. Voce esta com o PESO NORMAL.")
elif (25 <= imc < 30):
    print(f"Seu IMC é {imc:.3}. Voce esta SOBREPESO.")
else:
    print(f"Seu IMC é {imc:.3}. Voce esta com OBESIDADE.")
    
sleep(1)

# Condiçao da IDADE
if ( idade < 18):
    print(f"A sua meta calorica diaria, baseada em sua idade, é de 2200 calorias por dia.")
elif (18 <= idade < 60):
    print(f"A sua meta calorica diaria, baseada em sua idade, é de 2000 calorias por dia.")
else:
    print(f"A sua meta calorica diaria, baseada em sua idade, é de 1800 calorias por dia.")