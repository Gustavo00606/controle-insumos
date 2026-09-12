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
    if opcao == "1":
        estrutura = {}
        codigo = input("Digite o código: ")
        nome = input("Digite o nome do insumo: ")
        quantidade = float(input("Digite a quantidade: "))
        unidade_medida = input("Digite a unidade de medida: ")
        estoque_minimo = float(input("Digite o estoque minimo: "))
        estrutura.update({
            "codigo": codigo,
            "nome": nome,
            "quantidade": quantidade,
            "unidade_de_medida": unidade_medida,
            "estoque_minimo": estoque_minimo})
        insumos.append(estrutura)
        print("Insumo cadastrado")