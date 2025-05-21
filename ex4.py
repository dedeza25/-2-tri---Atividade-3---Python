# Laço while para exibir o menu continuamente
while True:
    # Exibe o menu
    print("\nMenu de Opções:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    
    # Solicita a escolha do usuário
    escolha = int(input("Escolha uma opção (1, 2 ou 3): "))
    
    # Verifica a opção escolhida
    if escolha == 1:
        print("Olá! Como vai você?")
    elif escolha == 2:
        print("Aqui você pode obter ajuda com o programa.")
    elif escolha == 3:
        print("Saindo... Até logo!")
        break  # Sai do laço while e encerra o programa
    else:
        print("Opção inválida! Por favor, escolha entre 1, 2 ou 3.")
