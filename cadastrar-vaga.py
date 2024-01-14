import csv

file_name = "informacoes_vagas.csv"

while True:
    day = input(
        "Adicione o dia que você se candidatou a essa vaga ou digite stop para encerrar: "
    )

    if day.lower() == "stop":
        break

    job = input("Digite o nome ou coloque o link da vaga: ")
    platform = input("Plataforma que usou para se candidatar: ")
    response = input("Você já teve retorno dessa vaga? S/N: ")
    obs = input("Alguma observação a mais? (se não só apertar Enter): ")
    result = input("Teve resposta positiva ou negativa? responda com P ou N ")



    with open(file_name, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            csv_writer.writerow(["Dia", "Vaga", "Plataforma", "retorno", "obs", "resultado"])

        csv_writer.writerow([day, job, platform, response, obs, result])

print("Informações salvas com sucesso no arquivo CSV.")
