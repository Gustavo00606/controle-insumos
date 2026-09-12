insumos = []

while True:
    print("\n===== CONTROLE DE INSUMOS =====")
    print("1 - Cadastrar insumo")
    print("2 - Listar insumos")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Consultar insumo")
    print("6 - Estoque baixo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado")
        break