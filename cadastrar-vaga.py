import csv

# Nome do arquivo CSV
name_file = 'informacoes_vagas.csv'

# Pede ao usuário para inserir informações até que ele decida parar
while True:
    day = input("Digite o dia que você se aplicou para essa vaga (ou 'parar' para encerrar): ")
    
    # Verifica se o usuário deseja parar
    if day.lower() == 'parar':
        break

    job = input("Digite o nome ou coloque o link da vaga: ")
    platform = input("Plataforma que usou para se candidatar: ")
    response = input("Você já teve retorno dessa vaga? S/N: ")
    obs = input("Alguma observação a mais? (se não só apertar Enter): ")



    # Abre o arquivo CSV em modo de escrita
    with open(name_file, mode='a', newline='') as arquivo_csv:
        # Cria um objeto escritor CSV
        escritor_csv = csv.writer(arquivo_csv)

        # Se o arquivo estiver vazio, adiciona cabeçalho
        if arquivo_csv.tell() == 0:
            escritor_csv.writerow(['Dia', 'Vaga', 'Plataforma', 'retorno', 'obs'])

        # Escreve as informações fornecidas pelo usuário
        escritor_csv.writerow([day, job, platform, response, obs])

print("Informações salvas com sucesso no arquivo CSV.")
