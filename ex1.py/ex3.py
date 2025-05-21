# Solicita três números inteiros ao usuário e armazena na lista 'numeros'
numeros = []
for i in range(3):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Cria uma nova lista com os números multiplicados por 2
numeros_multiplicados = [num * 2 for num in numeros]

# Exibe as duas listas
print("Lista original:", numeros)
print("Lista com números multiplicados por 2:", numeros_multiplicados)

# Calcula e exibe a soma dos números originais
soma_numeros = sum(numeros)
print("Soma dos números originais:", soma_numeros)

# Calcula e exibe a soma dos números multiplicados por 2
soma_multiplicados = sum(numeros_multiplicados)
print("Soma dos números multiplicados por 2:", soma_multiplicados)
