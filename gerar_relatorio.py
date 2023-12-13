from csv import DictReader


def generate_report(file_name):
    with open(file_name, mode="r", newline="") as csv_file:
        data_dict = [row for row in DictReader(csv_file)]
        result_total = f'Você já se candidatou a {len(data_dict)} vagas!'
        print(result_total)
        count_yes = 0
        count_not = 0
        for data in data_dict:
            if data['retorno'] == 'S':
                count_yes += 1
            else:
                count_not += 1
        result_counter = f'De todas as {len(data_dict)} vagas: {count_yes} tiveram retorno e {count_not} não tiveram retorno'
        print(result_counter)
   


generate_report("informacoes_vagas.csv")