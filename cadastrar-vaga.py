import csv

file_name = "job_information.csv"

while True:
    day = input("Enter the day you applied for this job (or 'stop' to end): ")

    if day.lower() == "stop":
        break

    job = input("Digite o nome ou coloque o link da vaga: ")
    platform = input("Plataforma que usou para se candidatar: ")
    response = input("Você já teve retorno dessa vaga? S/N: ")
    obs = input("Alguma observação a mais? (se não só apertar Enter): ")

    with open(file_name, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            csv_writer.writerow(["Dia", "Vaga", "Plataforma", "retorno", "obs"])

        csv_writer.writerow([day, job, platform, response, obs])

print("Informações salvas com sucesso no arquivo CSV.")
