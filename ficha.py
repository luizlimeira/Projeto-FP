import json
import os

ARQUIVO_FICHA = os.path.join(os.path.dirname(__file__), 'ficha.json')

def carregar_ficha():
    if not os.path.exists(ARQUIVO_FICHA):
        with open(ARQUIVO_FICHA, 'w') as f:
            json.dump([], f, indent=4)

    with open(ARQUIVO_FICHA, 'r') as f:
        return json.load(f)

def salvar_ficha(ficha):
    with open(ARQUIVO_FICHA, 'w') as f:
        json.dump(ficha, f, indent=4, ensure_ascii=False)

ficha_pratos = []
ficha_bebidas = []

def visualizar_ficha():
    while True: 
        print("1 - Visualizar Ficha Tecnica de Pratos")
        print("2- Visualizar Ficha Tecnica de Bebida")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            if not ficha_pratos:
                print("Nenhum prato cadastrado")
            else:
                print("\n--- Ficha Técnica - Pratos ---")
                for i, prato in enumerate(ficha_pratos):
                    print(f"{i+1}. Nome: {prato[0]}")
                    print(f"   Ingredientes: {prato[1]}")
                    print(f"   Modo de Preparo: {prato[2]}")
                    print("-" * 40)
                break
        elif opcao == 2:
            if not ficha_bebidas:
                print("Nenhuma bebida cadastrada")
            else:
                print("\n--- Ficha Técnica - Bebidas ---")
                for i, bebidas in enumerate(ficha_bebidas):
                    print(f"{i+1}. Nome: {bebidas[0]}")
                    print(f"   Ingredientes: {bebidas[1]}")
                    print(f"   Modo de Preparo: {bebidas[2]}")
                    print("-" * 40)
                break
        else:
            print("Escolha uma opcao válida")
            return

# def adicionar_usuario(nome, idade):
#     usuarios = carregar_usuarios()

#     usuarios.append({'nome': nome, 'idade': idade})

#     with open(arquivo, 'w') as f:
#         json.dump(usuarios, f, indent=4, ensure_ascii=False)
#     print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

# def atualizar_usuario(nome_antigo, novo_nome, nova_idade):
#     usuarios = carregar_usuarios()

#     for usuario in usuarios:
#         if usuario['nome'] == nome_antigo:
#             usuario['nome'] = novo_nome
#             usuario['idade'] = nova_idade
#             break

#     with open(arquivo, 'w') as f:
#         json.dump(usuarios, f, indent=4, ensure_ascii=False)
#     print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

# def excluir_usuario(nome):
#     usuarios = carregar_usuarios()

#     for usuario in usuarios:  
#         if usuario['nome'] == nome:
#             usuarios.remove(usuario)

#     with open(arquivo, 'w') as f:
#         json.dump(usuarios, f, indent=4, ensure_ascii=False)
#     print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")