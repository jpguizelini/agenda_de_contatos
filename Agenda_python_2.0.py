from pathlib import Path # importar a classe Path do modulo pathlib para trabalhar com diretorios 
import time # modulo manipular data e hora
import os # modulo comandos Windows 


dic_contatos = {}

# Função limpa terminal e retorna menu
def retornar_menu():
    time.sleep(1) 
    if os.name == 'nt': # caso S.O seja Windows
        os.system('cls')
    menu()

# Função inserir contatos
def inserir():
    campos = ['Nome', 'Telefone', 'Email', 'Twitter', 'Instagram']
    qnts = int(input('Quantos contatos deseja inserir?\t'))
    
    for _ in range(qnts):
        print('')
        contato = []
        for campo in campos:
            valor_campo = input(f'{campo}: ')
            contato.append(valor_campo)
        
        nome_contato = contato[0]
        dic_contatos[nome_contato] = contato  # Adiciona o contato à lista de contatos
    
    print('\nContato(s) inserido(s) com sucesso!')
    retornar_menu()

# Função consultar contato
def consulta():
    consulta = input('Qual contato deseja consultar?\t')
    if consulta in dic_contatos:
        contato = dic_contatos[consulta]
        print('')
        print(f'Nome: {contato[0]}')
        print(f'Telefone: {contato[1]}')
        print(f'Email: {contato[2]}')
        print(f'Twitter: {contato[3]}')
        print(f'Instagram: {contato[4]}')
    else:
        print('Contato não encontrado.')
    input('\nPressione ENTER para voltar ao menu.')
    retornar_menu()

# Função alterar contato
def alterar():
    nome_contato = input('Qual contato deseja alterar? \t ')
    if nome_contato in dic_contatos:
        contato = dic_contatos[nome_contato]
        print(f'Nome: {contato[0]}')
        print(f'Telefone: {contato[1]}')
        print(f'Email: {contato[2]}')
        print(f'Twitter: {contato[3]}')
        print(f'Instagram: {contato[4]}')

        print('\nAltere o contato:')
        campos = ['nome', 'telefone', 'email', 'twitter', 'instagram']
        for i, campo in enumerate(campos):
            novo_valor = input(f'{campo.capitalize()}: ')
            if novo_valor:
                contato[i] = novo_valor

        print("Contato alterado com sucesso!")
    else:
        print('Contato não encontrado.')
    retornar_menu()

# Função remover contatos
def remover():
    contato = input('Qual contato deseja remover?\t')
    if contato in dic_contatos:
        del dic_contatos[contato]
        print('Contato removido com sucesso!')
    else:
        print('Contato não encontrado.')
    retornar_menu()

# Função relatório mostrando todos os contatos
def relatorio():
    contador = 0
    print("Nome \t E-mail \t\t Telefone \t Twitter \t Instagram")
    for i in dic_contatos.keys():
        contador = contador + 1
        # Repare que i irá alterar a cada execução do for
        print("{} \t {} \t {} \t {} \t {}".format(i, dic_contatos[i][2], dic_contatos[i][1], dic_contatos[i][3], dic_contatos[i][4]))
    print("\nO número de usuários cadastrados é:", contador)
    print('Pressione ENTER para voltar ao menu')
    retornar_menu()

# Função para salvar dados separados por vírgula em um arquivo de texto na área de trabalho
def salvar():
    dados_formatados = "" # variável para armazenar os dados formatados
    for nome, contato in dic_contatos.items():
        telefone = contato[1]
        email = contato[2]
        twitter = contato[3]
        instagram = contato[4]

        linha = f"{nome},{telefone},{email},{twitter},{instagram}\n" # cria a string formatada
        dados_formatados += linha # vai adicionando as linhas aos dados formatados

    caminho_arquivo = Path.home() / "Desktop" / "contatos.txt" # Caminho completo do arquivo na área de trabalho
    with open(caminho_arquivo, "w") as arquivo: # Escreve os dados no arquivo

        arquivo.write(dados_formatados)
    print(f"Dados salvos em: {caminho_arquivo}") 
    print('Pressione ENTER para voltar ao menu ')
    retornar_menu()

# Função para sair do programa
def sair():
    print('Saindo...')
    time.sleep(1.5) 
    exit()

#- menu do programa
def menu():
    opcao_menu = {
    '1':inserir,
    '2':consulta,
    '3':alterar,
    '4':remover,
    '5':relatorio,
    '6':salvar,
    '7':sair,
    }
    opcao= (input('''  
    ############################
                Menu
    1) Inserir um contato ( um ou mais contatos)
    2) Consulta
    3) Alterar
    4) Remover
    5) Relatório todos os contatos
    6) Salvar dados (separados por virgula em um arquivo texto)
    7) Sair
    ###########################\n
    '''))
    if (opcao) in opcao_menu:
        time.sleep(1)
        if os.name == 'nt': # verifica se o sistema operacional é Windows 
            os.system('cls') # limpa console no Windows
        opcao_menu[(opcao)]()        
    else:
        print('Opção inválida')
        retornar_menu()
menu()
