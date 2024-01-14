from csv import DictReader


def search_info(file_name, name):
    with open(file_name, mode="r", newline="") as csv_file:
        data_dict = [row for row in DictReader(csv_file)]
        result = list()
        for data in data_dict:
            if name in data["Vaga"]:
                result.append(data)
        print(result)

        
        # for data in data_dict:
        #     if data['Vaga'] == name:









        


search_info("informacoes_vagas.csv", "Frete")