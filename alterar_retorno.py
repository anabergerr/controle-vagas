import csv

def update_return_by_job(job_name, new_return_value, new_result):
    file_name = "informacoes_vagas.csv"

    updated_lines = []

    with open(file_name, mode="r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)

        for line in lines:
            if job_name.lower() in line[1].lower():
                line[3] = new_return_value
                line[5] = new_result
            updated_lines.append(line)

    with open(file_name, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerows(updated_lines)


job_name_input = input("Digite o nome da vaga para alterar o retorno: ")
new_return_value_input = input("Digite o novo valor para a coluna retorno: ")
new_result = input("Digite o novo valor para a coluna resultado, P ou N: ")


update_return_by_job(job_name_input, new_return_value_input, new_result)

print("Valor da coluna 'retorno' atualizado com sucesso..")
