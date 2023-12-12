import csv

def alterar_retorno_por_vaga(nome_vaga, novo_retorno):
    # Nome do arquivo CSV
    name_file = 'informacoes_vagas.csv'

    # Lista para armazenar linhas atualizadas
    linhas_atualizadas = []

    # Abre o arquivo CSV em modo de leitura e escrita
    with open(name_file, mode='r', newline='') as arquivo_csv:
        # Cria um objeto leitor CSV
        leitor_csv = csv.reader(arquivo_csv)

        # Lê e armazena as linhas do arquivo CSV
        linhas = list(leitor_csv)

        # Percorre as linhas e procura pela vaga desejada
        for linha in linhas:
            if nome_vaga.lower() in linha[1].lower():
                # Atualiza o valor da coluna "retorno"
                linha[3] = novo_retorno

            # Adiciona a linha à lista de linhas atualizadas
            linhas_atualizadas.append(linha)

    # Abre o arquivo CSV em modo de escrita
    with open(name_file, mode='w', newline='') as arquivo_csv:
        # Cria um objeto escritor CSV
        escritor_csv = csv.writer(arquivo_csv)

        # Escreve as linhas atualizadas no arquivo
        escritor_csv.writerows(linhas_atualizadas)

# Exemplo de uso da função
nome_vaga_input = input("Digite o nome da vaga para alterar o retorno: ")
novo_retorno_input = input("Digite o novo valor para a coluna retorno: ")

alterar_retorno_por_vaga(nome_vaga_input, novo_retorno_input)

print("Valor da coluna 'retorno' atualizado com sucesso.")
