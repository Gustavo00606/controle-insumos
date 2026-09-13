insumos = []

def exibir_menu():
    print("\n===== CONTROLE DE INSUMOS =====")
    print("1 - Cadastrar insumo")
    print("2 - Listar insumos")
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
    print("5 - Consultar insumo")
    print("6 - Estoque baixo")
    print("0 - Sair")

def exibir_insumo(dicionario):
    print("-"*25)
    print (f"Código: {dicionario['codigo']}")
    print (f"Nome: {dicionario['nome']}")
    print (f"Quantidade: {dicionario['quantidade']} {dicionario['unidade_de_medida']}")
    print (f"Estoque mínimo: {dicionario['estoque_minimo']} {dicionario['unidade_de_medida']}")

def cadastrar_insumo(insumos):
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

def listar_insumos(insumos):
    if insumos == []:
        print("Nenhum insumo cadastrado")
    else:
        for dicionario in insumos:
            exibir_insumo(dicionario)
    print("-"*25)

def registrar_entrada(insumos):
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

def registrar_saida(insumos):
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

def consultar_insumo(insumos):
    encontrado = False
    cod = input("Qual o código do produto? ")
    for dicionario in insumos:
        if cod == dicionario["codigo"]:
            exibir_insumo(dicionario)
            encontrado = True
            break
    if encontrado == False:
        print("Este código não pertence a nenhum produto cadastrado")

def estoque_baixo(insumos):
    tem_estoque_baixo = False
    for dicionario in insumos:
        if dicionario["quantidade"] <= dicionario["estoque_minimo"]:
            exibir_insumo(dicionario)
            tem_estoque_baixo = True
    if tem_estoque_baixo == False:
        print("Nenhum insumo com estoque baixo")
    

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado")
        break

    if opcao == "1":
        cadastrar_insumo(insumos)

    if opcao == "2":
        listar_insumos(insumos)

    if opcao == "3":
        registrar_entrada(insumos)

    if opcao == "4":
        registrar_saida(insumos)

    if opcao == "5":
        consultar_insumo(insumos)
    if opcao == "6":
        estoque_baixo(insumos)