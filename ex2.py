# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Lista de vogais (maiúsculas e minúsculas)
vogais = 'aeiouAEIOU'

# Inicializa a variável que vai contar as vogais
contador_vogais = 0

# Laço for para percorrer cada letra da palavra
for letra in palavra:
    if letra in vogais:
        contador_vogais += 1

# Imprime o total de vogais
print("Total de vogais:", contador_vogais)
