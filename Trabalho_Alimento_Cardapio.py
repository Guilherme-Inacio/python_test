# Usando a funçao TIME
from time import sleep

usuario = input(str("Digite o seu nome: ")).strip().title()

# Adicionando as listas
alimentos = []
alimentos_saudaveis = []
alimentos_nao_saudaveis = []
alimentos_desconhecidos = []

# Indice I para a contagem 
i = 0

print(f"Olá, {usuario}.")

# Usuario informando os 5 alimentos 
print("Informe os 5 alimentos que voce mais consome no dia a dia.")
while i < 5:
    ali = input(str(f"Informe o {i+1} alimento: ")).lower().strip()
    alimentos.append(ali)
    i = i + 1

# Transformando a lista em um string unica com .join()
comida_usuario = ", ".join(alimentos).title()
sleep(1)
print(f"Os alimentos que voce digitou: {comida_usuario}")

# Lista de alimentos saudaveis e nao saudaveis 
saudaveis = ["maça","banana","uva","morango","laranja","mamao","aveia","brocolis","cenoura","berinjela","tomate","alface","salada","legume","verdura"]
nao_saudaveis = ["brigadeiro","chocolate","fritura","pao","doce","salgadinho","miojo","hamburguer"]

# Repetiçao para a verificaçao das listas e adicianando os alimentos nas respectivas listas
for comida in alimentos:
    if comida in saudaveis:
        alimentos_saudaveis.append(comida)
    elif comida in nao_saudaveis:
        alimentos_nao_saudaveis.append(comida)
    else:
        alimentos_desconhecidos.append(comida)
        
sleep(1)

# Printando para o usuario o resultado final 
comida_saudavel = ", ".join(alimentos_saudaveis).title()
print(f"Alimentos considerados saudaveis: {comida_saudavel}.")
comida_nao_saudavel = ", ".join(alimentos_nao_saudaveis).title()
print(f"Alimentos considerados nao saudaveis: {comida_nao_saudavel}.")
comida_desconhecida = ", ".join(alimentos_desconhecidos).title()
print(f"Alimentos desconhecidos pelo aplicativo: {comida_desconhecida}.\n")
sleep(0.8)
print("------------------FIM------------------\n")


# APLICATIVO DE CARDAPIO SEMANAL
sleep(1)

print("Criando o cardapio de alimentos da semana")

# Criando o dicionario chamado cardapio
cardapio = { 
    "Segunda-Feira" : [],
    "Terça-Feira" : [],
    "Quarta-Feira" : [],
    "Quinta-Feira" : [],
    "Sexta-Feira" : [],
    "Sabado" : [],
    "Domingo" : [],
}

# Preenchendo as listas dentro do dicionario
for dia in cardapio:
    print(f"Informe o cardapio de {dia}.")
    # Informando os alimentos dos dias
    for a in range(0,5):
        comidas_dias = input(str(f"informe o {a+1}  alimento: ")).strip().lower()
        cardapio[dia].append(comidas_dias)

sleep(1)

# Printando para o usuario
for dia in cardapio:
    comida =", ".join(cardapio[dia])
    print(f"{dia}: {comida}\n")

sleep(0.8)
print("------------------FIM------------------")