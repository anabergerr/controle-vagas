from csv import DictReader


def generate_report(file_name):
    with open(file_name, mode="r", newline="") as csv_file:
        data_dict = [row for row in DictReader(csv_file)]
        result_total = f"Você já se candidatou a {len(data_dict)} vagas!"
        print(result_total)
        count_yes = 0
        count_not = 0
        count_result = 0
        for data in data_dict:
            if data["retorno"].upper() == "S":
                count_yes += 1
            if data["resultado"] == "P":
                count_result += 1
            else:
                count_not += 1
        result_counter = f"De todas as vagas:\n{count_yes} tiveram retorno,\n{count_not} não tiveram retorno ainda e \n{count_result} deram continuidade no processo"
        print(result_counter)


generate_report("informacoes_vagas.csv")
