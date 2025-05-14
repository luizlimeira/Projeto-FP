import json
import os

ARQUIVO_FICHA_TECNICA = os.path.join(os.path.dirname(__file__), 'Ficha-Técnica.json')

def carregar_ficha():
    # Verifica se o arquivo existe, se não existir, cria um arquivo com lista vazia
    if not os.path.exists(ARQUIVO_FICHA):
        with open(ARQUIVO_FICHA, 'w') as f:
            json.dump([], f, indent=4)
    
    # Carrega o conteúdo do arquivo
    with open(ARQUIVO_FICHA, 'r') as f:
        return json.load(f)

# def salvar_ficha(ficha): (oq é isso?)

def visualizar_ficha():
    while true: 
        print("1 - Visualizar Ficha Tecnica de Pratos")
        print("2- Visualizar Ficha Tecnica de Bebida")
        opcao = int(input())

        if opcao == 1:
            pratos[[], []] 
            break
        elif opcao == 2:
            bebidas[[], []]
            break
        else:
            print("Escolha uma opcao válida")
            return


#     if usuarios:
#         print("=" *50)
#         print("LISTA DE USUÁRIOS:")
#         print("-" *50)
#         for usuario in usuarios:
#             print("*" *50)
#             print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
#             print("*" *50)
#             print("=" *50)
#     else:
#         print("😒 NENHUM USUÁRIO CADASTRADO.")

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