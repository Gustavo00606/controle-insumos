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
    if opcao == "2":
        if insumos == []:
            print("Nenhum insumo cadastrado")
        else:
            for dicionario in insumos:
                print("-"*25)
                print (f"Código: {dicionario['codigo']}")
                print (f"Nome: {dicionario['nome']}")
                print (f"Quantidade: {dicionario['quantidade']} {dicionario['unidade_de_medida']}")
                print (f"Estoque mínimo: {dicionario['estoque_minimo']} {dicionario['unidade_de_medida']}")
        print("-"*25)
    if opcao == "3":
        encontrado = False
        cod = input("Qual o código do produto? ")
        for dicionario in insumos:
            if cod == dicionario["codigo"]:
                entrada = float(input("Qual quantidade entrou? "))
                if entrada > 0:
                    dicionario["quantidade"] += entrada
                    print("Estoque atualizado")
                else:
                    print("Entrada invalida")
                encontrado = True
                break
        if encontrado == False:
            print("Este código não pertence a nenhum produto cadastrado")
    if opcao == "4":
                encontrado = False
                cod = input("Qual o código do produto? ")
                for dicionario in insumos:
                    if cod == dicionario["codigo"]:
                        saida = float(input("Qual quantidade saiu? "))
                        if saida <= 0:
                            print("Saída inválida")
                        else:
                            if saida <= dicionario["quantidade"]:
                                dicionario["quantidade"] -= saida
                                print("Estoque atualizado")
                            else:
                                print(f"A saída é maior que a quantidade atual do estoque({dicionario['quantidade']})")
                        encontrado = True
                        break
                if encontrado == False:
                    print("Este código não pertence a nenhum produto cadastrado")
    if opcao == "5":
        encontrado = False
        cod = input("Qual o código do produto? ")
        for dicionario in insumos:
            if cod == dicionario["codigo"]:
                print("-"*25)
                print (f"Código: {dicionario['codigo']}")
                print (f"Nome: {dicionario['nome']}")
                print (f"Quantidade: {dicionario['quantidade']} {dicionario['unidade_de_medida']}")
                print (f"Estoque mínimo: {dicionario['estoque_minimo']} {dicionario['unidade_de_medida']}")
                encontrado = True
                break
        if encontrado == False:
            print("Este código não pertence a nenhum produto cadastrado")